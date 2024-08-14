#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    # Set up the URL and headers
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

    try:
        # Make the request to the Reddit API
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the request was successful
        if response.status_code == 200:
            data = response.json()
            # Return the number of subscribers
            return data['data']['subscribers']
        else:
            # If the subreddit is invalid, return 0
            return 0
    except requests.RequestException:
        # Handle any request errors
        return 0

# Example usage:
subreddit_name = "learnpython"
subscribers = number_of_subscribers(subreddit_name)
print(f"Subscribers in '{subreddit_name}': {subscribers}")
