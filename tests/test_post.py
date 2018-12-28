from twitterbot import post_factory
from twitterbot.post import (
    Post,
    Media,
    News,
    Teaser,
    BehindTheScenes,
    DanceCover,
)
import pytest


class MockPost:
    def __init__(
        self,
        id,
        title,
        flair,
        link="https://i.redd.it/x394xmn28s521.png",
        is_video=False,
    ):
        self.id = id
        self.title = title
        self.link_flair_text = flair
        self.url = link
        self.is_video = is_video


@pytest.mark.parametrize(
    "input,expected_class",
    [
        (MockPost("abc332", "Test News", "[News]"), News),
        (
            MockPost("red127", "Test BTS", "[Behind-The-Scenes]"),
            BehindTheScenes,
        ),
        (MockPost("asdprq", "Test Dance Cover", "[Dance Cover]"), DanceCover),
    ],
)
def test_factory(input, expected_class):
    assert isinstance(post_factory(input), expected_class)


@pytest.mark.parametrize("input", [MockPost("abc123", "Test Post", "Post")])
def test_instantiate_base_class(input):
    with pytest.raises(TypeError):
        Post(input)


@pytest.mark.parametrize("input", [MockPost("abc123", "Test Post", "Post")])
def test_instantiate_media_class(input):
    with pytest.raises(TypeError):
        Media(input)

