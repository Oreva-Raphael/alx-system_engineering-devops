#!/usr/bin/python3
"""
request and display data from reddit
"""

from requests import get


def top_ten(subreddit):
    """
    This function queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit
    """
    if not (subreddit and isinstance(subreddit, str)):
        print("None")
    try:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        user_agent = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
            "AppleWebKit/537.36"}
        response = get(url, headers=user_agent)
        result = response.json()["data"]["children"]
        for item in result:
            print(item['data']['title'])
    except Exception:
        print("None")
