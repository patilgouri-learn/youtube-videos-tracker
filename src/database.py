import sqlite3
from pathlib import Path


DATABASE_PATH = Path("data/youtube_tracker.db")


def get_connection():
    DATABASE_PATH.parent.mkdir(exist_ok=True)

    return sqlite3.connect(DATABASE_PATH)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS videos (
            video_id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            channel TEXT NOT NULL,
            published_at TEXT NOT NULL,
            description TEXT,
            thumbnail_url TEXT,
            category TEXT,
            discovered_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    connection.commit()
    connection.close()


def video_exists(video_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        "SELECT 1 FROM videos WHERE video_id = ?",
        (video_id,)
    )

    result = cursor.fetchone()

    connection.close()

    return result is not None


def save_video(video):
    if video_exists(video["video_id"]):
        return False

    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO videos (
            video_id,
            title,
            channel,
            published_at,
            description,
            thumbnail_url,
            category
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        video["video_id"],
        video["title"],
        video["channel"],
        video["published_at"],
        video["description"],
        video["thumbnail_url"],
        video["category"]
    ))

    connection.commit()
    connection.close()

    return True


if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfully!")