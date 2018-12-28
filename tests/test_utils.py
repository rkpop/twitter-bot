from twitterbot import sanitize_flair
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [
        ("[News]", "News"),
        ("[Dance Cover]", "DanceCover"),
        ("[Behind-The-Scenes]", "BehindTheScenes"),
    ],
)
def test_sanitize_flair(input, expected):
    assert sanitize_flair(input) == expected
