from CONFIG import OAUTH_CLIENT,OAUTH_SECRET,REDDIT_UNAME,REDDIT_PASS,USER_AGENT
from database_check import db_checking
import praw

def main():
    reddit = praw.Reddit(client_id=OAUTH_CLIENT,client_secret=OAUTH_SECRET,user_agent=USER_AGENT,username=REDDIT_UNAME,password=REDDIT_PASS)
    subreddit = reddit.subreddit('kpop')
    while True:
        submissions = (submission for submission in subreddit.hot() if (submission.score >= 100))
        new_submission = db_checking(submissions)
        for submission in new_submission:
            #status = tweet(submission)
            print("{title}:{id}:{point}".format(title=submission.title,id=submission.id,point=submission.score))
        
 
if __name__ == '__main__':
    main()