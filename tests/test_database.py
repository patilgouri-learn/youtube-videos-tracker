import sqlite3

from src import database


def test_video_can_be_saved(tmp_path, monkeypatch):

    test_database = tmp_path / "test.db"

    monkeypatch.setattr(
        database,
        "DATABASE_PATH",
        test_database
    )

    database.initialize_database()

    video = {
        "video_id": "A2uYpG8F83T_d86L",
        "title": "DevOps Reality| No code field #devops",
        "channel": "Chandni",
        "published_at": "2026-09-03T07:07:19Z",
        "description": "DevOps is a highly paid job in today's market.",
        "thumbnail_url": "https://img.youtube.com/vi/A2uYpG8F83T_d86L/hqdefault.jpg",
        "category": "devops"
    }

    result = database.save_video(video)

    assert result is True
    assert database.video_exists("A2uYpG8F83T_d86L") is True


def test_duplicate_video_is_not_saved(tmp_path, monkeypatch):

    test_database = tmp_path / "test.db"

    monkeypatch.setattr(
        database,
        "DATABASE_PATH",
        test_database
    )

    database.initialize_database()

    video = {
        "video_id": "A2uYpG8F83T_d86L",
        "title": "DevOps Reality| No code field #devops",
        "channel": "Chandni",
        "published_at": "2026-09-03T07:07:19Z",
        "description": "DevOps is a highly paid job in today's market.",
        "thumbnail_url": "https://img.youtube.com/vi/A2uYpG8F83T_d86L/hqdefault.jpg",
        "category": "devops"
    }

    first_insert = database.save_video(video)
    second_insert = database.save_video(video)

    assert first_insert is True
    assert second_insert is False