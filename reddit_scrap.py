import praw
import pandas as pd

#creating an instance of Reddit. Create an app from this link https://www.reddit.com/prefs/apps to get the following credentials. 
reddit = praw.Reddit(client_id = 'client_id', client_secret ='client_secret', user_agent='user_agent')

#scrap data from the LiverpoolFC subreddit
posts = reddit.subreddit('LiverpoolFC').hot(limit = 2000)

c = ['title', 'name', 'url', 'score', 'locked', 'created', 'num of comment', 'upvote ratio']
df = pd.DataFrame(([post.title, post.name, post.url, post.score, post.locked, post.created, post.num_comments, post.upvote_ratio] for post in posts), columns = c)
df.to_csv('liverpool_subreddit.csv')
