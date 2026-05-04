from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from activitysmith_openapi.configuration import Configuration
from activitysmith_openapi.api_client import ApiClient

from activitysmith_openapi.api.live_activities_api import LiveActivitiesApi
from activitysmith_openapi.api.metrics_api import MetricsApi
from activitysmith_openapi.api.push_notifications_api import PushNotificationsApi

SDK_VERSION = "1.2.2"
SDK_HEADER_NAME = "X-ActivitySmith-SDK"
SDK_HEADER_VALUE = f"python-v{SDK_VERSION}"


def _request_value(request: Any, key: str) -> Any:
    if isinstance(request, dict):
        return request.get(key)

    return getattr(request, key, None)


def _has_media(request: Any) -> bool:
    media = _request_value(request, "media")
    if isinstance(media, str):
        return media.strip() != ""
    return media is not None


def _has_actions(request: Any) -> bool:
    actions = _request_value(request, "actions")
    if actions is None:
        return False
    if isinstance(actions, (list, tuple, set, dict)):
        return len(actions) > 0
    return True


def _validate_push_request(request: Any) -> Any:
    if _has_media(request) and _has_actions(request):
        raise ValueError("ActivitySmith: media cannot be combined with actions")
    return request


def _metric_value_request(value_or_request: Any, timestamp: Any | None = None) -> Any:
    if isinstance(value_or_request, dict) and "value" in value_or_request:
        if timestamp is None:
            return value_or_request

        request = dict(value_or_request)
        request["timestamp"] = timestamp
        return request

    request = {"value": value_or_request}
    if timestamp is not None:
        request["timestamp"] = timestamp

    return request


def _normalize_channels_target(request: Any) -> Any:
    if not isinstance(request, dict):
        return request

    if "target" in request or "channels" not in request:
        return request

    normalized = dict(request)
    raw_channels = normalized.pop("channels")

    channels: list[str] = []
    if isinstance(raw_channels, str):
        channels = [item.strip() for item in raw_channels.split(",") if item.strip() != ""]
    elif isinstance(raw_channels, (list, tuple)):
        channels = [item.strip() for item in raw_channels if isinstance(item, str) and item.strip() != ""]

    if channels:
        normalized["target"] = {"channels": channels}

    return normalized


class NotificationsResource:
    def __init__(self, api: PushNotificationsApi) -> None:
        self._api = api

    def send(self, request: Any):
        normalized = _validate_push_request(_normalize_channels_target(request))
        return self._api.send_push_notification(
            push_notification_request=normalized
        )

    # Backward-compatible alias.
    def send_push_notification(self, push_notification_request: Any):
        return self.send(push_notification_request)


class LiveActivitiesResource:
    def __init__(self, api: LiveActivitiesApi) -> None:
        self._api = api

    def start(self, request: Any):
        return self._api.start_live_activity(
            live_activity_start_request=_normalize_channels_target(request)
        )

    def update(self, request: Any):
        return self._api.update_live_activity(live_activity_update_request=request)

    def end(self, request: Any):
        return self._api.end_live_activity(live_activity_end_request=request)

    def stream(self, stream_key: str, request: Any):
        return self._api.reconcile_live_activity_stream(
            stream_key=stream_key,
            live_activity_stream_request=_normalize_channels_target(request),
        )

    def end_stream(self, stream_key: str, request: Any | None = None):
        return self._api.end_live_activity_stream(
            stream_key=stream_key,
            live_activity_stream_delete_request=request,
        )

    # Backward-compatible aliases.
    def start_live_activity(self, live_activity_start_request: Any):
        return self.start(live_activity_start_request)

    def update_live_activity(self, live_activity_update_request: Any):
        return self.update(live_activity_update_request)

    def end_live_activity(self, live_activity_end_request: Any):
        return self.end(live_activity_end_request)

    def reconcile_live_activity_stream(self, stream_key: str, live_activity_stream_request: Any):
        return self.stream(stream_key, live_activity_stream_request)

    def end_live_activity_stream(self, stream_key: str, live_activity_stream_delete_request: Any | None = None):
        return self.end_stream(stream_key, live_activity_stream_delete_request)


class MetricsResource:
    def __init__(self, api: MetricsApi) -> None:
        self._api = api

    def update(self, key: str, value_or_request: Any, timestamp: Any | None = None):
        return self._api.update_metric_value(
            key=key,
            metric_value_update_request=_metric_value_request(value_or_request, timestamp),
        )

    # Backward-compatible generated-style alias.
    def update_metric_value(self, key: str, metric_value_update_request: Any):
        return self._api.update_metric_value(
            key=key,
            metric_value_update_request=metric_value_update_request,
        )


@dataclass
class ActivitySmith:
    api_key: str

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("ActivitySmith: api_key is required")

        config = Configuration(access_token=self.api_key)

        api_client = ApiClient(configuration=config)
        api_client.user_agent = f"activitysmith-python/{SDK_VERSION}"
        api_client.set_default_header(SDK_HEADER_NAME, SDK_HEADER_VALUE)

        self.notifications = NotificationsResource(PushNotificationsApi(api_client))
        self.live_activities = LiveActivitiesResource(LiveActivitiesApi(api_client))
        self.metrics = MetricsResource(MetricsApi(api_client))
