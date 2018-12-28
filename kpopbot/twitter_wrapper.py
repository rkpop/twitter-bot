from twitter import Twitter, OAuth


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
        self.uploading_instance = Twitter(
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
            self._text_only(post)

    def _text_only(self, post):
        pass

    def _with_media(self, post):
        pass

    def _upload_media(self, image_url):
        pass
