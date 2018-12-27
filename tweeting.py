from twitter import TwitterHTTPError
from CONSTANTS import TEMPLATES


def tweet(instance, content):
    post = TEMPLATES[content["type"]].format(
        id=content["id"], title=content["title"]
    )
    try:
        instance.statuses.update(status=post)
    except TwitterHTTPError:
        pass
