###########################################################################
# Tests of third-party modules
###########################################################################
import os

from .utils import assert_


def test_lru_dict():
    "The LRUDict binary module can be used"
    from lru import LRU
    lru_dict = LRU(5)

    # Add 10 items
    for i in range(10):
        lru_dict[f"item_{i}"] = i

    # Items 0-4 have been evicted
    for i in range(5):
        assert_(f"item_{i}" not in lru_dict)
    # Items 5-9 are still there
    for i in range(5, 10):
        assert_(lru_dict[f"item_{i}"] == i)


def test_pillow():
    "Pillow can be used to load images"
    from PIL import Image

    for extension in ['png', 'jpg']:
        image = Image.open(
            os.path.join(
                os.path.dirname(__file__),
                "resources",
                f"test-pattern.{extension}"
            )
        )
        assert_(image.size == (1366, 768))
