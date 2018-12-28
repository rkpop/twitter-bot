from kpopbot import (
    PRAWWrapper,
    TwitterWrapper,
    Database,
    post_factory,
    sanitize_flair,
    WHITELIST,
)
from CONFIG import REDDIT_CONFIG, TWITTER_CONFIG, DB_URL, TABLE_NAME


def main():
    reddit = PRAWWrapper(REDDIT_CONFIG)
    twitter = TwitterWrapper(TWITTER_CONFIG)
    database = Database(DB_URL, TABLE_NAME)
    while True:
        posts = (
            post_factory(post)
            for post in reddit.obtain_posts()
            if database.check_table(post.id)
            and (
                post.link_flair_text is not None
                and sanitize_flair(post.link_flair_text) in WHITELIST
            )
        )
        for post in posts:
            twitter.tweet(post)
            database.write_table(post.post_id)


if __name__ == "__main__":
    main()
