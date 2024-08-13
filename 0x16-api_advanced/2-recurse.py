#!/usr/bin/python3
"""Function to query a list of all hot posts on a given Reddit subreddit."""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot posts on a given subreddit."""
    pathname = "https://www.reddit.com/r/{}/hot.json?limit=100"
    url = pathname.format(subreddit)
    headers = {"User-Agent": "reddit-{}".format(subreddit)}
    params = {"after": after} if after else None

    response = requests.get(
            url,
            headers=headers,
            params=params,
            allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json().get("data")
        if data and data.get("children"):
            for post in data.get("children"):
                hot_list.append(post.get("data").get("title"))
            after = data.get("after")
            if after:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
    return None
