import os
import requests
from dotenv import load_dotenv


load_dotenv()

API_KEY = os.getenv("YOUTUBE_API_KEY")

BASE_URL = "https://www.googleapis.com/youtube/v3/search"


def get_recent_videos(query, max_results=10):
    params = {
        "part": "snippet",
        "q": query,
        "type": "video",
        "order": "date",
        "maxResults": max_results,
        "key": API_KEY,
    }

    response = requests.get(BASE_URL, params=params, timeout=30)

    response.raise_for_status()

    return response.json()


if __name__ == "__main__":
    videos = get_recent_videos("devops")

    for video in videos.get("items", []):
        snippet = video["snippet"]

        print("=" * 60)
        print("Title:", snippet["title"])
        print("Channel:", snippet["channelTitle"])
        print("Published:", snippet["publishedAt"])