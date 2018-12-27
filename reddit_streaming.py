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
        new_submission = db_checking(submissions)
        for submission in new_submission:
            if submission.link_flair_text in WHITELIST:
                content = {
                    "id": submission.id,
                    "title": submission.title,
                    "type": submission.link_flair_text,
                }
                tweet(twitter, content)
                write_to_db(submission.id)


if __name__ == "__main__":
    main()
