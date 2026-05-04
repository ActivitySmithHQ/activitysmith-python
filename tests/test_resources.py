from importlib.metadata import version

from activitysmith.client import ActivitySmith
import activitysmith.client as client_module


class FakePushNotificationsApi:
    def __init__(self, _api_client):
        self._api_client = _api_client
        self.calls = []

    def send_push_notification(self, **kwargs):
        self.calls.append(kwargs)
        return kwargs


class FakeLiveActivitiesApi:
    def __init__(self, _api_client):
        self._api_client = _api_client
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

    def reconcile_live_activity_stream(self, **kwargs):
        self.calls.append(("stream", kwargs))
        return kwargs

    def end_live_activity_stream(self, **kwargs):
        self.calls.append(("end_stream", kwargs))
        return kwargs


class FakeMetricsApi:
    def __init__(self, _api_client):
        self._api_client = _api_client
        self.calls = []

    def update_metric_value(self, **kwargs):
        self.calls.append(kwargs)
        return kwargs


def test_sdk_header_and_user_agent_are_configured(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    api_client = client.metrics._api._api_client

    package_version = version("activitysmith")
    assert api_client.default_headers["X-ActivitySmith-SDK"] == f"python-v{package_version}"
    assert api_client.default_headers["User-Agent"] == f"activitysmith-python/{package_version}"


def test_notifications_short_and_legacy_alias(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

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


def test_notifications_map_channels_to_target(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    payload = {"title": "Build Failed", "channels": ["devs", "ops"]}

    client.notifications.send(payload)
    client.notifications.send_push_notification({"title": "Build Failed", "channels": "devs,ops"})

    assert client.notifications._api.calls == [
        {"push_notification_request": {"title": "Build Failed", "target": {"channels": ["devs", "ops"]}}},
        {"push_notification_request": {"title": "Build Failed", "target": {"channels": ["devs", "ops"]}}},
    ]


def test_notifications_preserve_media_and_redirection(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    payload = {
        "title": "Voice Over Generated",
        "media": "https://cdn.activitysmith.com/voice_over.mp3",
        "redirection": "https://studio.acme.com/voice-overs/482/review",
    }

    client.notifications.send(payload)

    assert client.notifications._api.calls == [
        {"push_notification_request": payload},
    ]


def test_notifications_reject_media_and_actions(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    try:
        client.notifications.send(
            {
                "title": "Voice Over Generated",
                "media": "https://cdn.activitysmith.com/voice_over.mp3",
                "actions": [{"title": "Open", "type": "open_url", "url": "https://example.com"}],
            }
        )
    except ValueError as exc:
        assert str(exc) == "ActivitySmith: media cannot be combined with actions"
    else:
        raise AssertionError("Expected ValueError for media + actions")


def test_live_activities_short_and_legacy_aliases(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

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


def test_live_activities_start_maps_channels_to_target(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    payload = {
        "content_state": {
            "title": "Deploy",
            "number_of_steps": 4,
            "current_step": 1,
            "type": "segmented_progress",
        },
        "channels": ["devs", "ops"],
    }

    client.live_activities.start(payload)
    client.live_activities.start_live_activity(payload)

    expected = {
        "content_state": {
            "title": "Deploy",
            "number_of_steps": 4,
            "current_step": 1,
            "type": "segmented_progress",
        },
        "target": {"channels": ["devs", "ops"]},
    }
    assert client.live_activities._api.calls == [
        ("start", {"live_activity_start_request": expected}),
        ("start", {"live_activity_start_request": expected}),
    ]


def test_live_activities_support_progress_payloads(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    payload = {
        "content_state": {
            "title": "Render export",
            "subtitle": "encoding frames",
            "type": "progress",
            "percentage": 67,
            "color": "purple",
        }
    }

    client.live_activities.start(payload)

    assert client.live_activities._api.calls == [
        ("start", {"live_activity_start_request": payload}),
    ]


def test_live_activities_stream_short_and_legacy_aliases(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    stream_payload = {
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 9, "unit": "%"},
                {"label": "MEM", "value": 45, "unit": "%"},
            ],
        },
        "channels": ["ops"],
    }
    end_payload = {
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 7, "unit": "%"},
                {"label": "MEM", "value": 38, "unit": "%"},
            ],
        }
    }

    client.live_activities.stream("prod-web-1", stream_payload)
    client.live_activities.end_stream("prod-web-1", end_payload)
    client.live_activities.reconcile_live_activity_stream("prod-web-1", stream_payload)
    client.live_activities.end_live_activity_stream("prod-web-1", end_payload)

    expected_stream = {
        "content_state": stream_payload["content_state"],
        "target": {"channels": ["ops"]},
    }
    assert client.live_activities._api.calls == [
        (
            "stream",
            {
                "stream_key": "prod-web-1",
                "live_activity_stream_request": expected_stream,
            },
        ),
        (
            "end_stream",
            {
                "stream_key": "prod-web-1",
                "live_activity_stream_delete_request": end_payload,
            },
        ),
        (
            "stream",
            {
                "stream_key": "prod-web-1",
                "live_activity_stream_request": expected_stream,
            },
        ),
        (
            "end_stream",
            {
                "stream_key": "prod-web-1",
                "live_activity_stream_delete_request": end_payload,
            },
        ),
    ]


def test_live_activities_pass_action_payloads_through(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    start_payload = {
        "content_state": {
            "title": "Deploying payments-api",
            "subtitle": "Running database migrations",
            "number_of_steps": 5,
            "current_step": 3,
            "type": "segmented_progress",
        },
        "action": {
            "title": "Open Workflow",
            "type": "open_url",
            "url": "https://github.com/acme/payments-api/actions/runs/1234567890",
        },
    }

    update_payload = {
        "activity_id": "act-1",
        "content_state": {
            "title": "Reindexing product search",
            "subtitle": "Shard 7 of 12",
            "number_of_steps": 12,
            "current_step": 7,
        },
        "action": {
            "title": "Pause Reindex",
            "type": "webhook",
            "url": "https://ops.example.com/hooks/search/reindex/pause",
            "method": "POST",
            "body": {"job_id": "reindex-2026-03-19"},
        },
    }

    end_payload = {
        "activity_id": "act-1",
        "content_state": {
            "title": "Deploying payments-api",
            "subtitle": "Production rollout complete",
            "number_of_steps": 5,
            "current_step": 5,
        },
        "action": {
            "title": "Open Workflow",
            "type": "open_url",
            "url": "https://github.com/acme/payments-api/actions/runs/1234567890",
        },
    }

    client.live_activities.start(start_payload)
    client.live_activities.update(update_payload)
    client.live_activities.end(end_payload)

    assert client.live_activities._api.calls == [
        ("start", {"live_activity_start_request": start_payload}),
        ("update", {"live_activity_update_request": update_payload}),
        ("end", {"live_activity_end_request": end_payload}),
    ]


def test_metrics_short_and_legacy_aliases(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    client.metrics.update(
        "deploy.success_rate",
        99.9,
        timestamp="2026-05-03T12:30:00.000Z",
    )
    client.metrics.update("prod.status", {"value": "healthy"})
    client.metrics.update_metric_value("deploy.success_rate", {"value": 42})

    assert client.metrics._api.calls == [
        {
            "key": "deploy.success_rate",
            "metric_value_update_request": {
                "value": 99.9,
                "timestamp": "2026-05-03T12:30:00.000Z",
            },
        },
        {
            "key": "prod.status",
            "metric_value_update_request": {"value": "healthy"},
        },
        {
            "key": "deploy.success_rate",
            "metric_value_update_request": {"value": 42},
        },
    ]
