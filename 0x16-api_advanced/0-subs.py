#!/usr/bin/python3
"""
request and use data from reddit
"""

from requests import get


def number_of_subscribers(subreddit):
    """
    A function to query Reddit API and return the number of subscribers
    """
    if not (subreddit and isinstance(subreddit, str)):
        return 0

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    user_agent = {'User-Agent': 'Arc Chromium Engine Version 129.0.6668.59'}
    response = get(url, headers=user_agent)
    results = response.json

    try:
        return results.get('data').get('subscribers')
    except Exception:
        return 0
