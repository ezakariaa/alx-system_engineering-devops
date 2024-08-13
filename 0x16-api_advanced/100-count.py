#!/usr/bin/python3
"""Function to count words in all hot posts of a given Reddit subreddit."""
import requests


def count_words(subreddit, word_list, after=None, word_counts={}):
    """Prints counts of given words found in hot posts of a given subreddit.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of words to search for in post titles.
        word_counts (obj): Key/value pairs of words/counts.
        after (str): The parameter for the next page of the API results.
    """
    if not word_list:
        sorted_counts = sorted(
                word_counts.items(),
                key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
        return

    word = word_list.pop(0).lower()
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
                title = post.get("data").get("title").lower()
                wrding = word_counts.get(word, 0)
                titling = title.count(word)
                word_counts[word] = wrding + titling
            after = data.get("after")
            if after:
                return count_words(subreddit, word_list, after, word_counts)
            else:
                return count_words(subreddit, word_list, None, word_counts)

    if word_list:
        count_words(subreddit, word_list, None, word_counts)
    else:
        sorted_counts = sorted(
                word_counts.items(),
                key=lambda x: (-x[1], x[0])
        )
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))
