from importlib.metadata import version

from activitysmith.client import ActivitySmith, action, alert_badge, alert_icon, content_state, metric
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


class FakeAppIconBadgesApi:
    def __init__(self, _api_client):
        self._api_client = _api_client
        self.calls = []

    def update_app_icon_badge_count(self, **kwargs):
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


def test_badge_count_clears_and_targets_channels(monkeypatch):
    monkeypatch.setattr(client_module, "AppIconBadgesApi", FakeAppIconBadgesApi)

    client = ActivitySmith(api_key="x")

    cleared = client.badge_count(0)
    targeted = client.badge_count(3, channels="sales,customer-success")

    assert cleared == {"app_icon_badge_count_update_request": {"badge": 0}}
    assert targeted == {
        "app_icon_badge_count_update_request": {
            "badge": 3,
            "target": {"channels": ["sales", "customer-success"]},
        }
    }
    assert client._app_icon_badges.calls == [cleared, targeted]


def test_notifications_named_fields(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    client.notifications.send(
        title="New subscription 💸",
        message="Customer upgraded to Pro plan",
        channels="sales,customer-success",
    )

    assert client.notifications._api.calls == [
        {
            "push_notification_request": {
                "title": "New subscription 💸",
                "message": "Customer upgraded to Pro plan",
                "target": {"channels": ["sales", "customer-success"]},
            }
        },
    ]


def test_push_action_helper(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    client.notifications.send(
        title="New subscription 💸",
        actions=[
            action(
                title="Open CRM Profile",
                type="open_url",
                url="shortcuts://run-shortcut?name=Open%20CRM",
            )
        ],
    )

    assert client.notifications._api.calls == [
        {
            "push_notification_request": {
                "title": "New subscription 💸",
                "actions": [
                    {
                        "title": "Open CRM Profile",
                        "type": "open_url",
                        "url": "shortcuts://run-shortcut?name=Open%20CRM",
                    }
                ],
            }
        },
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
    client.notifications.send(
        title="Run Shortcut",
        redirection="shortcuts://run-shortcut?name=Jarvis",
    )

    assert client.notifications._api.calls == [
        {"push_notification_request": payload},
        {
            "push_notification_request": {
                "title": "Run Shortcut",
                "redirection": "shortcuts://run-shortcut?name=Jarvis",
            }
        },
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


def test_live_activities_support_timer_payloads(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    client.live_activities.start(
        title="Benchmark Run",
        subtitle="sampling performance",
        type=client.live_activities.TYPE_TIMER,
        duration_seconds=300,
        counts_down=True,
        color="cyan",
    )
    client.live_activities.update(
        activity_id="act-1",
        title="Benchmark Run",
        type=client.live_activities.TYPE_TIMER,
        subtitle="complete",
        color="cyan",
    )

    assert client.live_activities._api.calls == [
        (
            "start",
            {
                "live_activity_start_request": {
                    "content_state": {
                        "title": "Benchmark Run",
                        "subtitle": "sampling performance",
                        "type": "timer",
                        "duration_seconds": 300,
                        "counts_down": True,
                        "color": "cyan",
                    }
                }
            },
        ),
        (
            "update",
            {
                "live_activity_update_request": {
                    "activity_id": "act-1",
                    "content_state": {
                        "title": "Benchmark Run",
                        "type": "timer",
                        "subtitle": "complete",
                        "color": "cyan",
                    },
                }
            },
        ),
    ]


def test_live_activities_support_stats_payloads(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    payload = {
        "content_state": {
            "title": "Sales",
            "subtitle": "last hour",
            "type": client.live_activities.TYPE_STATS,
            "metrics": [
                {"label": "Revenue", "value": "$2430", "color": "blue"},
                {"label": "Orders", "value": "37", "color": "green"},
                {"label": "Conversion", "value": "4.8%", "color": "magenta"},
            ],
        }
    }

    client.live_activities.start(payload)

    assert client.live_activities._api.calls == [
        ("start", {"live_activity_start_request": payload}),
    ]


def test_live_activities_support_alert_helpers(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    state_payload = content_state(
        title="Reactivation",
        message="Lumen came back after 2 weeks",
        type=client.live_activities.TYPE_ALERT,
        icon=alert_icon("cloud.sun", color="yellow"),
        badge=alert_badge("Customer", color="magenta"),
        color="red",
    )

    client.live_activities.stream("customer-ops", content_state=state_payload)
    client.live_activities.update(
        activity_id="act-1",
        title="Onboarding",
        message="A customer is stuck at workspace setup",
        type=client.live_activities.TYPE_ALERT,
        icon=client.live_activities.alert_icon("person.crop.circle.badge.questionmark"),
        badge=client.live_activities.alert_badge("Customer", color="gray"),
        color="red",
    )

    assert client.live_activities._api.calls == [
        (
            "stream",
            {
                "stream_key": "customer-ops",
                "live_activity_stream_request": {
                    "content_state": {
                        "title": "Reactivation",
                        "message": "Lumen came back after 2 weeks",
                        "type": client.live_activities.TYPE_ALERT,
                        "color": "red",
                        "icon": {"symbol": "cloud.sun", "color": "yellow"},
                        "badge": {"title": "Customer", "color": "magenta"},
                    },
                },
            },
        ),
        (
            "update",
            {
                "live_activity_update_request": {
                    "activity_id": "act-1",
                    "content_state": {
                        "title": "Onboarding",
                        "message": "A customer is stuck at workspace setup",
                        "type": client.live_activities.TYPE_ALERT,
                        "color": "red",
                        "icon": {"symbol": "person.crop.circle.badge.questionmark"},
                        "badge": {"title": "Customer", "color": "gray"},
                    },
                }
            },
        ),
    ]


def test_live_activities_support_icon_and_badge_on_non_alert_types(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")

    client.live_activities.stream(
        "prod-web-1",
        content_state=content_state(
            title="Server Health",
            subtitle="prod-web-1",
            type=client.live_activities.TYPE_METRICS,
            icon=alert_icon("server.rack", color="blue"),
            metrics=[metric(label="CPU", value=18, unit="%")],
        ),
    )
    client.live_activities.stream(
        "nightly-database-backup",
        content_state=content_state(
            title="Nightly Database Backup",
            subtitle="verify restore",
            type=client.live_activities.TYPE_PROGRESS,
            badge=alert_badge("S3", color="cyan"),
            percentage=62,
        ),
    )

    assert client.live_activities._api.calls == [
        (
            "stream",
            {
                "stream_key": "prod-web-1",
                "live_activity_stream_request": {
                    "content_state": {
                        "title": "Server Health",
                        "subtitle": "prod-web-1",
                        "type": client.live_activities.TYPE_METRICS,
                        "icon": {"symbol": "server.rack", "color": "blue"},
                        "metrics": [{"label": "CPU", "value": 18, "unit": "%"}],
                    },
                },
            },
        ),
        (
            "stream",
            {
                "stream_key": "nightly-database-backup",
                "live_activity_stream_request": {
                    "content_state": {
                        "title": "Nightly Database Backup",
                        "subtitle": "verify restore",
                        "type": client.live_activities.TYPE_PROGRESS,
                        "badge": {"title": "S3", "color": "cyan"},
                        "percentage": 62,
                    },
                },
            },
        ),
    ]


def test_live_activities_build_requests_from_named_fields(monkeypatch):
    monkeypatch.setattr(client_module, "PushNotificationsApi", FakePushNotificationsApi)
    monkeypatch.setattr(client_module, "LiveActivitiesApi", FakeLiveActivitiesApi)
    monkeypatch.setattr(client_module, "MetricsApi", FakeMetricsApi)

    client = ActivitySmith(api_key="x")
    metrics = [
        metric(label="CPU", value=9, unit="%"),
        client.live_activities.metric(label="MEM", value=45, unit="%"),
    ]
    action_payload = action(
        title="Open Dashboard",
        type="open_url",
        url="shortcuts://run-shortcut?name=Open%20Dashboard",
    )
    secondary_action_payload = action(
        title="Deny",
        type="webhook",
        url="https://ops.example.com/hooks/server-health/deny",
        method="POST",
    )
    state_payload = content_state(
        title="Server Health",
        subtitle="prod-web-1",
        type=client.live_activities.TYPE_METRICS,
        metrics=metrics,
    )

    client.live_activities.start(
        content_state=state_payload,
        action=action_payload,
        secondary_action=secondary_action_payload,
        channels=["ops"],
    )
    client.live_activities.update(
        activity_id="act-1",
        title="Server Health",
        subtitle="prod-web-1",
        type=client.live_activities.TYPE_METRICS,
        metrics=metrics,
        secondary_action=secondary_action_payload,
    )
    client.live_activities.end(
        activity_id="act-1",
        title="Server Health",
        subtitle="prod-web-1",
        type=client.live_activities.TYPE_METRICS,
        metrics=metrics,
        auto_dismiss_minutes=2,
        secondary_action=secondary_action_payload,
    )

    assert client.live_activities._api.calls == [
        (
            "start",
            {
                "live_activity_start_request": {
                    "content_state": {
                        "title": "Server Health",
                        "subtitle": "prod-web-1",
                        "type": client.live_activities.TYPE_METRICS,
                        "metrics": metrics,
                    },
                    "action": action_payload,
                    "secondary_action": secondary_action_payload,
                    "target": {"channels": ["ops"]},
                }
            },
        ),
        (
            "update",
            {
                "live_activity_update_request": {
                    "activity_id": "act-1",
                    "content_state": {
                        "title": "Server Health",
                        "subtitle": "prod-web-1",
                        "type": client.live_activities.TYPE_METRICS,
                        "metrics": metrics,
                    },
                    "secondary_action": secondary_action_payload,
                }
            },
        ),
        (
            "end",
            {
                "live_activity_end_request": {
                    "activity_id": "act-1",
                    "content_state": {
                        "title": "Server Health",
                        "subtitle": "prod-web-1",
                        "type": client.live_activities.TYPE_METRICS,
                        "metrics": metrics,
                        "auto_dismiss_minutes": 2,
                    },
                    "secondary_action": secondary_action_payload,
                }
            },
        ),
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
            "url": "shortcuts://run-shortcut?name=Deploy%20Status",
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
            "url": "shortcuts://run-shortcut?name=Deploy%20Status",
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
