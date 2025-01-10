import pandas as pd
import praw
import datetime
from praw.models import MoreComments
import csv


user_agent = "fido_scraper"
reddit = praw.Reddit (
client_id="lbZdfbSoH0mjXgP3Nu463g",
client_secret="xvhLaiATaCp_cG-H5sjXFj7HPZQeqg",
user_agent=user_agent
)

data = {
    # "ID": [],
    # "TITLE": [],
    # "SELFTEXT": [],
    # "AUTHOR": [],
    # "URL": [],
    # "COMMENTS":[]
}

everything = []
df_list = []

ids = []
# title = []
# selftext = []
# author = []
# url = []
all_comments=[]
# comments = []

headlines = set()

for submission in reddit.subreddit('Passkeys').hot(limit=2000):

    submission.comments.replace_more(limit=None)
    i=1
    top_level_comments = list(submission.comments)
    all_comments = submission.comments.list()
    headlines.add(submission.title)
    ids.append(submission.id)
    # data["ID"].append(submission.id)
    # time = submission.created
    # data["TITLE"].append(submission.title)
    # data["SELFTEXT"].append(submission.selftext)
    # data["AUTHOR"].append(submission.author)
    # data["URL"].append(submission.url)
i = 1
for id in ids:
    submission=reddit.submission(id)
    print("\nNew Thread: "+id+"\n")
    
    submission.comments.replace_more(limit=1)
    f=open("data2/data"+str(i)+".txt","w")
    n=1
    for comment in submission.comments.list():
      f.write("Comment "+str(n)+": "+comment.body)
      n+=1
    i+=1
    f.close()
      # all_comments=''.join("Comment "+str(i)+": "+comment.body)
    # data["COMMENTS"].append(all_comments)  

# df = pd.DataFrame(data)

# df.to_csv('reddit_passkeys.csv', index=False)

# # Download the CSV file to your local computer
# from google.colab import files
# files.download('reddit_passkeys.csv')