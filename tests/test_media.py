from kpopbot.media import first_image, media_provider
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [("https://imgur.com/a/l0N2w80", "https://i.imgur.com/qju1Npw.jpg")],
)
def test_first_image(input, expected):
    assert first_image(input) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        (
            "https://i.redd.it/x394xmn28s521.png",
            "https://i.redd.it/x394xmn28s521.png",
        ),
        ("https://i.imgur.com/jxiRKD7.png", "https://i.imgur.com/jxiRKD7.png"),
        ("https://imgur.com/a/l0N2w80", "https://i.imgur.com/qju1Npw.jpg"),
        ("https://www.vlive.tv/video/104884", None),
    ],
)
def test_media_provider(input, expected):
    assert media_provider(input) == expected
