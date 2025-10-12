import os
import requests
from dotenv import load_dotenv

# Let's load our secret API key from the .env file
# Build a reliable path to the .env file, no matter where the script is run from.
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
# Load the .env file using the specific path.
load_dotenv(dotenv_path=dotenv_path)

API_KEY = os.getenv("NEWS_API_KEY")

# The base URL for the 'everything' endpoint of the News API
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

def search_news(topic):
    """
    Searches for news articles on a specific topic using the News API.
    """
    if not API_KEY:
        # A safety check to make sure the API key is set.
        return None, "API Key is missing. Please check your .env file."

    print(f"Searching for news about: {topic}...")
    
    # We create a dictionary of parameters to send to the API.
    # 'q': the user's topic
    # 'language': we'll stick to English
    # 'pageSize': how many articles to get (let's grab 10)
    # 'apiKey': our secret key
    params = {
        'q': topic,
        'language': 'en',
        'pageSize': 10,
        'apiKey': API_KEY,
    }

    try:
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        # The API returns data in JSON format, which is easy to work with in Python.
        data = response.json()

        if data.get("status") == "ok":
            # The request was successful!
            articles = data.get("articles", [])
            print(f"Found {len(articles)} articles.")
            return articles, None # Return the list of articles and no error
        else:
            # Something went wrong on the API's end.
            error_message = data.get("message", "An unknown error occurred with the News API.")
            print(f"News API Error: {error_message}")
            return None, error_message

    except requests.RequestException as e:
        print(f"Network error when calling News API: {e}")
        return None, f"A network error occurred: {e}"

# We no longer need the 'fetch_article_content' function here.
# The News API gives us the content directly, which is much more reliable!
