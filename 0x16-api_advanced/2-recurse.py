#!/usr/bin/python3
"""
request and display data from the Reddit API
"""

import requests
after = None


def recurse(subreddit, hot_list=[]):
    """return a list containing the titles of all hot articles 
    for a given subreddit recursively"""
    
