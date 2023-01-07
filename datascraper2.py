from datetime import datetime
from newsapi import NewsApiClient
import praw
import pandas as pd

def reddit():
    reddit_authorized = praw.Reddit(client_id="",client_secret="",user_agent="", username="", password="")

    subreddit = reddit_authorized.subreddit("all")

    posts = subreddit.top(time_filter = "day")

    posts_dict = {"Title": [], "Post text": [], "Post URL": []}

    for post in posts:
        posts_dict["Title"].append(post.title)
        posts_dict["Post text"].append(post.selftext)
        posts_dict["Post URL"].append(post.url)

    top_posts = pd.DataFrame(posts_dict)
    print(top_posts)


def allNews():
    api = NewsApiClient(api_key='')

    all_articles = api.get_top_headlines(language='en')
    
    ListOfArticles = []

    for item in all_articles['articles'][1:10]:
        article = {}
        article['Author'] = item['author']
        article['Title'] = item['title']
        article['Body'] = item['content']
        article['Image'] = item['urlToImage']
        article['Link'] = item['url']
        article['ArType'] = 'article'
        article['Date'] = datetime.today().strftime('%Y-%m-%d')
        ListOfArticles.append(article)
    
    return ListOfArticles


reddit()
