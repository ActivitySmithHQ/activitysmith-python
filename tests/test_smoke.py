import os
from activitysmith import ActivitySmith

def test_client_constructs():
    client = ActivitySmith(api_key=os.getenv("ACTIVITYSMITH_API_KEY", "x"))
    assert client.notifications is not None
    assert client.live_activities is not None