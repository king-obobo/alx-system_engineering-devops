#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses the title of all
hot articles, and prints a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:oxo16.api.advanced:v1.0.0"
            }
    params = {
            "after": after,
            "count": count,
            "limit": 100
            }
    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    try:
        results = res.json()
        if res.status_code == 404:
            raise Exception
    except Exception:
        print("")
        return

    results = results.get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        title = c.get("data").get("title").lower().split()
        times_appeared = {}
        for word in word_list:
            times_appeared[word] = [word.lower() for word in
                                    word_list].count(word)
            if word in title:
                times = len([t for t in title if t == word.lower()])
                if instances.get(word) is None:
                    instances[word] = times
                else:
                    instances[word] += times

    if after is None:
        if len(instances) == 0:
            print("")
            return
        for item in times_appeared.keys():
            val = instances.get(item)
            if val is not None:
                instances[item] *= times_appeared.get(item)
        instances = sorted(instances.items(), key=lambda kv: (-kv[1], kv[0]))
        [print("{}: {}".format(k, v)) for k, v in instances]
    else:
        count_words(subreddit, word_list, instances, after, count)
