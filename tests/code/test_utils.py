import tempfile
from pathlib import Path

import numpy as np

from tagifai import utils


def test_load_json_from_url():
    tags_url = "https://raw.githubusercontent.com/GokuMohandas/MadeWithML/main/datasets/tags.json"
    tags_dict = {}
    for item in utils.load_json_from_url(url=tags_url):
        key = item.pop("tag")
        tags_dict[key] = item
    assert "natural-language-processing" in tags_dict


def test_save_and_load_dict():
    with tempfile.TemporaryDirectory() as dp:
        d = {"hello": "world"}
        fp = Path(dp, "d.json")
        utils.save_dict(d=d, filepath=fp)
        d = utils.load_dict(filepath=fp)
        assert d["hello"] == "world"


def test_set_seed():
    utils.set_seeds()
    a = np.random.randn(2, 3)
    b = np.random.randn(2, 3)
    utils.set_seeds()
    x = np.random.randn(2, 3)
    y = np.random.randn(2, 3)
    assert np.array_equal(a, x)
    assert np.array_equal(b, y)
