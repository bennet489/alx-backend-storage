#!/usr/bin/env python3
import requests
import time
from functools import lru_cache


@lru_cache(maxsize=None)
def get_page(url: str) -> str:
    # Increment the count for this URL
    increment_url_count(url)

    # Fetch the page content
    response = requests.get(url)

    # Check if the response is successful
    if response.status_code == 200:
        return response.text
    else:
        return f"Error: Failed to fetch page content for URL: {url}"


def increment_url_count(url: str) -> None:
    count_key = f"count:{url}"
    count = int(get_cached_count(count_key))
    count += 1
    set_cached_count(count_key, count)


@lru_cache(maxsize=None)
def get_cached_count(key: str) -> str:
    # Returns the count for the given key from cache, or 0 if not found
    return str(0)


def set_cached_count(key: str, value: int) -> None:
    # Sets the count for the given key in cache
    pass


if __name__ == "__main__":
    # Testing the get_page function
    url = "http://slowwly.robertomurray.co.uk/delay/1000/url/http://www.example.com"
    start_time = time.time()
    page_content = get_page(url)
    end_time = time.time()
    print(f"Page content:\n{page_content}")
    print(f"Time taken: {end_time - start_time} seconds")
