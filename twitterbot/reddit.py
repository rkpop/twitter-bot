from CONFIG import REDDIT_CONFIG
from CONSTANTS import WHITELIST
from praw import Reddit
from .utils import sanitize_flair as sf


class PRAWWrapper:
    def __init__(self, config):
        self.instance = Reddit(**REDDIT_CONFIG).subreddit("kpop")

    def obtain_posts(self):
        return (
            submission
            for submission in self.instance.hot()
            if (submission.score >= 100)
        )
