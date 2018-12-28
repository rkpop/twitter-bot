from praw import Reddit


class PRAWWrapper:
    def __init__(self, config):
        self.instance = Reddit(**config).subreddit("kpop")

    def obtain_posts(self):
        return (
            submission
            for submission in self.instance.hot()
            if (submission.score >= 100)
        )
