#!/usr/bin/python3
""" a function that queries the Reddit API and returns the number of subscrib
ers for a given subreddit."""
import requests


def number_of_subscribers(subreddit):
    """Returnd the total no of subscribers in a subraddit"""
    URL = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-agent": "linux:0x016.api.advanced:v1.0.0"
    }
    res = requests.get(URL, headers = headers, allow_redirects = False)
    if res.status_code == "404":
        return 0
    results = res.json().get("data")
    return results.get("subscribers")
