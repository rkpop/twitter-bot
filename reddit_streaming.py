from CONFIG import (
    OAUTH_CLIENT,
    OAUTH_SECRET,
    REDDIT_UNAME,
    REDDIT_PASS,
    USER_AGENT,
    TW_TOKEN,
    TW_TOKEN_SECRET,
    TW_API_KEY,
    TW_API_SECRET,
)
from CONSTANTS import WHITELIST
from database_func import db_checking, write_to_db
from tweeting import tweet
import praw
from twitter import *


def main():
    reddit = praw.Reddit(
        client_id=OAUTH_CLIENT,
        client_secret=OAUTH_SECRET,
        user_agent=USER_AGENT,
        username=REDDIT_UNAME,
        password=REDDIT_PASS,
    )
    subreddit = reddit.subreddit("kpop")
    twitter = Twitter(
        auth=OAuth(TW_TOKEN, TW_TOKEN_SECRET, TW_API_KEY, TW_API_SECRET),
        retry=5,
    )
    while True:
        submissions = (
            submission
            for submission in subreddit.hot()
            if (submission.score >= 100)
        )
        for submission in submissions:
            post_flair = (
                submission.link_flair_text.strip("[").strip("]")
                if submission.link_flair_text is not None
                else "Misc"
            )
            if post_flair in WHITELIST:
                content = {
                    "id": submission.id,
                    "title": submission.title,
                    "type": post_flair,
                }
                tweet(twitter, content)
                write_to_db(submission.id)


if __name__ == "__main__":
    main()
