from activitysmith.client import ActivitySmith
import activitysmith.client as client_module


class FakePushNotificationsApi:
    def __init__(self, _api_client):
        self.calls = []

    def send_push_notification(self, **kwargs):
        self.calls.append(kwargs)
        return kwargs


class FakeLiveActivitiesApi:
    def __init__(self, _api_client):
        self.calls = []

    def start_live_activity(self, **kwargs):
        self.calls.append(("start", kwargs))
        return kwargs

    def update_live_activity(self, **kwargs):
        self.calls.append(("update", kwargs))
        return kwargs

    def end_live_activity(self, **kwargs):
        self.calls.append(("end", kwargs))
        return kwargs


def test_notifications_short_and_legacy_alias(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)

    client = ActivitySmith(api_key="x")
    payload = {"title": "Build Failed"}

    short = client.notifications.send(payload)
    legacy = client.notifications.send_push_notification(payload)

    assert short == {"push_notification_request": payload}
    assert legacy == {"push_notification_request": payload}
    assert client.notifications._api.calls == [
        {"push_notification_request": payload},
        {"push_notification_request": payload},
    ]


def test_live_activities_short_and_legacy_aliases(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)

    client = ActivitySmith(api_key="x")
    start_payload = {
        "content_state": {
            "title": "Deploy",
            "number_of_steps": 4,
            "current_step": 1,
            "type": "segmented_progress",
        }
    }
    update_payload = {
        "activity_id": "act-1",
        "content_state": {"title": "Deploy", "current_step": 2},
    }
    end_payload = {
        "activity_id": "act-1",
        "content_state": {"title": "Deploy", "current_step": 4},
    }

    client.live_activities.start(start_payload)
    client.live_activities.update(update_payload)
    client.live_activities.end(end_payload)

    client.live_activities.start_live_activity(start_payload)
    client.live_activities.update_live_activity(update_payload)
    client.live_activities.end_live_activity(end_payload)

    assert client.live_activities._api.calls == [
        ("start", {"live_activity_start_request": start_payload}),
        ("update", {"live_activity_update_request": update_payload}),
        ("end", {"live_activity_end_request": end_payload}),
        ("start", {"live_activity_start_request": start_payload}),
        ("update", {"live_activity_update_request": update_payload}),
        ("end", {"live_activity_end_request": end_payload}),
    ]
