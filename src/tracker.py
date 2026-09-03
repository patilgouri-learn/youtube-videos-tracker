from database import initialize_database, save_video
from youtube_api import get_recent_videos


SEARCH_QUERIES = [
    "Devops Engineering",
    "Cloud Engineering",
    "Azure Engineering",
]


def extract_video_data(item, category):
    snippet = item["snippet"]

    return {
        "video_id": item["id"]["videoId"],
        "title": snippet["title"],
        "channel": snippet["channelTitle"],
        "published_at": snippet["publishedAt"],
        "description": snippet["description"],
        "thumbnail_url": snippet["thumbnails"]["high"]["url"],
        "category": category
    }


def track_videos():
    initialize_database()

    total_new_videos = 0

    for query in SEARCH_QUERIES:

        print(f"\nSearching for: {query}")

        response = get_recent_videos(
            query=query,
            max_results=10
        )

        for item in response.get("items", []):

            video = extract_video_data(
                item,
                category=query
            )

            is_new = save_video(video)

            if is_new:
                total_new_videos += 1
                print(f"NEW: {video['title']}")

            else:
                print(f"EXISTS: {video['title']}")

    print("\n" + "=" * 50)
    print(f"Tracking completed. New videos found: {total_new_videos}")
    print("=" * 50)


if __name__ == "__main__":
    track_videos()