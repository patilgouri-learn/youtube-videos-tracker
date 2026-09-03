from src.tracker import extract_video_data


def test_extract_video_data():
    sample_item = {
        "id": {
            "videoId": "A2uYpG8F83T_d86L"
        },
        "snippet": {
            "title": "DevOps Reality| No code field #devops",
            "channelTitle": "Chandni",
            "publishedAt": "2026-09-03T07:07:19Z",
            "description": "DevOps is a highly paid job in today's market.",
            "thumbnails": {
                "high": {
                    "url": "https://img.youtube.com/vi/A2uYpG8F83T_d86L/hqdefault.jpg"
                }
            }
        }
    }

    result = extract_video_data(
        sample_item,
        category="devops"
    )

    assert result["video_id"] == "A2uYpG8F83T_d86L"
    assert result["title"] == "DevOps Reality| No code field #devops"
    assert result["channel"] == "Chandni"
    assert result["category"] == "devops"