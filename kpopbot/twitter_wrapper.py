from kpopbot import HEADER
from twitter import Twitter, OAuth, TwitterHTTPError
from requests import get
from io import BytesIO


class TwitterWrapper(object):
    def __init__(self, details):
        self.instance = Twitter(
            auth=OAuth(
                details["token_key"],
                details["token_secret"],
                details["API_key"],
                details["API_secret"],
            )
        )
        self.uploader_instance = Twitter(
            domain="upload.twitter.com",
            auth=OAuth(
                details["token_key"],
                details["token_secret"],
                details["API_key"],
                details["API_secret"],
            ),
        )

    def tweet(self, post):
        if post._with_media:
            self._with_media(post)
        else:
            self._text_only(post)

    def _text_only(self, post):
        try:
            self.instance.statuses.update(status=post.nice)
        except TwitterHTTPError:
            pass

    def _with_media(self, post):
        imageid = self._upload_media(post.image_url)
        try:
            self.instance.statuses.update(
                status=post.nice, media_ids=str(imageid)
            )
        except TwitterHTTPError:
            pass

    def _upload_media(self, image_url):
        filedata = BytesIO(get(image_url, headers=HEADER).content).read()
        return self.uploader_instance.media.upload(media=filedata)[
            "media_id_string"
        ]
