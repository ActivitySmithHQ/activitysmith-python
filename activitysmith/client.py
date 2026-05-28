from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from activitysmith_openapi.configuration import Configuration
from activitysmith_openapi.api_client import ApiClient

from activitysmith_openapi.api.live_activities_api import LiveActivitiesApi
from activitysmith_openapi.api.metrics_api import MetricsApi
from activitysmith_openapi.api.push_notifications_api import PushNotificationsApi

SDK_VERSION = "1.5.0"
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


def _compact_dict(values: dict[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in values.items() if value is not None}


def metric(
    label: str,
    value: Any,
    *,
    unit: str | None = None,
    color: str | None = None,
) -> dict[str, Any]:
    return _compact_dict(
        {
            "label": label,
            "value": value,
            "unit": unit,
            "color": color,
        }
    )


def action(
    title: str,
    type: str,
    url: str,
    *,
    method: str | None = None,
    body: Any | None = None,
) -> dict[str, Any]:
    return _compact_dict(
        {
            "title": title,
            "type": type,
            "url": url,
            "method": method,
            "body": body,
        }
    )


def alert_icon(
    symbol: str,
    *,
    color: str | None = None,
) -> dict[str, Any]:
    return _compact_dict(
        {
            "symbol": symbol,
            "color": color,
        }
    )


def alert_badge(
    title: str,
    *,
    color: str | None = None,
) -> dict[str, Any]:
    return _compact_dict(
        {
            "title": title,
            "color": color,
        }
    )


def _normalize_live_activity_content_state(content_state: Any) -> Any:
    return content_state


def content_state(
    title: str,
    *,
    type: str | None = None,
    subtitle: str | None = None,
    message: str | None = None,
    icon: Any | None = None,
    badge: Any | None = None,
    metrics: Any | None = None,
    number_of_steps: int | None = None,
    current_step: int | None = None,
    percentage: int | float | None = None,
    value: int | float | None = None,
    upper_limit: int | float | None = None,
    color: str | None = None,
    step_color: str | None = None,
    auto_dismiss_seconds: int | None = None,
    auto_dismiss_minutes: int | None = None,
) -> dict[str, Any]:
    state = _compact_dict(
        {
            "title": title,
            "subtitle": subtitle,
            "type": type,
            "message": message,
            "icon": icon,
            "badge": badge,
            "metrics": metrics,
            "number_of_steps": number_of_steps,
            "current_step": current_step,
            "percentage": percentage,
            "value": value,
            "upper_limit": upper_limit,
            "color": color,
            "step_color": step_color,
            "auto_dismiss_seconds": auto_dismiss_seconds,
            "auto_dismiss_minutes": auto_dismiss_minutes,
        }
    )
    return _normalize_live_activity_content_state(state)


def _build_push_request(
    request: Any | None,
    *,
    title: Any | None = None,
    message: Any | None = None,
    subtitle: Any | None = None,
    media: Any | None = None,
    redirection: Any | None = None,
    actions: Any | None = None,
    target: Any | None = None,
    channels: Any | None = None,
) -> Any:
    request_fields = _compact_dict(
        {
            "title": title,
            "message": message,
            "subtitle": subtitle,
            "media": media,
            "redirection": redirection,
            "actions": actions,
            "target": target,
            "channels": channels,
        }
    )

    if not request_fields:
        return request

    if request is None:
        normalized: dict[str, Any] = {}
    elif isinstance(request, dict):
        normalized = dict(request)
    else:
        raise TypeError(
            "ActivitySmith: named push notification fields can only be combined with a dict request"
        )

    normalized.update(request_fields)
    return normalized


class LiveActivityColor:
    LIME = "lime"
    GREEN = "green"
    CYAN = "cyan"
    BLUE = "blue"
    PURPLE = "purple"
    MAGENTA = "magenta"
    RED = "red"
    ORANGE = "orange"
    YELLOW = "yellow"
    GRAY = "gray"


def _build_live_activity_request(
    request: Any | None,
    *,
    activity_id: Any | None = None,
    content_state: Any | None = None,
    title: Any | None = None,
    subtitle: Any | None = None,
    type: Any | None = None,
    message: Any | None = None,
    icon: Any | None = None,
    badge: Any | None = None,
    metrics: Any | None = None,
    number_of_steps: Any | None = None,
    current_step: Any | None = None,
    percentage: Any | None = None,
    value: Any | None = None,
    upper_limit: Any | None = None,
    color: Any | None = None,
    step_color: Any | None = None,
    auto_dismiss_seconds: Any | None = None,
    auto_dismiss_minutes: Any | None = None,
    action: Any | None = None,
    alert: Any | None = None,
    target: Any | None = None,
    channels: Any | None = None,
) -> Any:
    content_state_fields = _compact_dict(
        {
            "title": title,
            "subtitle": subtitle,
            "type": type,
            "message": message,
            "icon": icon,
            "badge": badge,
            "metrics": metrics,
            "number_of_steps": number_of_steps,
            "current_step": current_step,
            "percentage": percentage,
            "value": value,
            "upper_limit": upper_limit,
            "color": color,
            "step_color": step_color,
            "auto_dismiss_seconds": auto_dismiss_seconds,
            "auto_dismiss_minutes": auto_dismiss_minutes,
        }
    )
    content_state_fields = _normalize_live_activity_content_state(content_state_fields)
    request_fields = _compact_dict(
        {
            "activity_id": activity_id,
            "action": action,
            "alert": alert,
            "target": target,
            "channels": channels,
        }
    )

    if content_state is None and not content_state_fields and not request_fields:
        return request

    if request is None:
        normalized: dict[str, Any] = {}
    elif isinstance(request, dict):
        normalized = dict(request)
    else:
        raise TypeError(
            "ActivitySmith: named Live Activity fields can only be combined with a dict request"
        )

    if content_state is not None:
        content_state = _normalize_live_activity_content_state(content_state)
        existing_content_state = normalized.get("content_state")
        if existing_content_state is None:
            normalized["content_state"] = content_state
        elif isinstance(existing_content_state, dict) and isinstance(content_state, dict):
            normalized["content_state"] = {**existing_content_state, **content_state}
        else:
            raise TypeError("ActivitySmith: content_state must be a dict")

    if content_state_fields:
        existing_content_state = normalized.get("content_state")
        if existing_content_state is None:
            normalized["content_state"] = content_state_fields
        elif isinstance(existing_content_state, dict):
            normalized["content_state"] = {**existing_content_state, **content_state_fields}
        else:
            raise TypeError("ActivitySmith: content_state must be a dict")
        normalized["content_state"] = _normalize_live_activity_content_state(
            normalized["content_state"]
        )

    normalized.update(request_fields)
    return normalized


class NotificationsResource:
    def __init__(self, api: PushNotificationsApi) -> None:
        self._api = api

    def send(
        self,
        request: Any | None = None,
        *,
        title: Any | None = None,
        message: Any | None = None,
        subtitle: Any | None = None,
        media: Any | None = None,
        redirection: Any | None = None,
        actions: Any | None = None,
        target: Any | None = None,
        channels: Any | None = None,
    ):
        request = _build_push_request(
            request,
            title=title,
            message=message,
            subtitle=subtitle,
            media=media,
            redirection=redirection,
            actions=actions,
            target=target,
            channels=channels,
        )
        normalized = _validate_push_request(_normalize_channels_target(request))
        return self._api.send_push_notification(
            push_notification_request=normalized
        )

    # Backward-compatible alias.
    def send_push_notification(self, push_notification_request: Any | None = None, **fields: Any):
        return self.send(push_notification_request, **fields)


class LiveActivitiesResource:
    TYPE_SEGMENTED_PROGRESS = "segmented_progress"
    TYPE_PROGRESS = "progress"
    TYPE_METRICS = "metrics"
    TYPE_STATS = "stats"
    TYPE_ALERT = "alert"

    def __init__(self, api: LiveActivitiesApi) -> None:
        self._api = api

    @staticmethod
    def metric(
        label: str,
        value: Any,
        *,
        unit: str | None = None,
        color: str | None = None,
    ) -> dict[str, Any]:
        return metric(label, value, unit=unit, color=color)

    @staticmethod
    def alert_icon(
        symbol: str,
        *,
        color: str | None = None,
    ) -> dict[str, Any]:
        return alert_icon(symbol, color=color)

    @staticmethod
    def alert_badge(
        title: str,
        *,
        color: str | None = None,
    ) -> dict[str, Any]:
        return alert_badge(title, color=color)

    def start(
        self,
        request: Any | None = None,
        *,
        content_state: Any | None = None,
        title: Any | None = None,
        subtitle: Any | None = None,
        type: Any | None = None,
        message: Any | None = None,
        icon: Any | None = None,
        badge: Any | None = None,
        metrics: Any | None = None,
        number_of_steps: Any | None = None,
        current_step: Any | None = None,
        percentage: Any | None = None,
        value: Any | None = None,
        upper_limit: Any | None = None,
        color: Any | None = None,
        step_color: Any | None = None,
        action: Any | None = None,
        alert: Any | None = None,
        target: Any | None = None,
        channels: Any | None = None,
    ):
        request = _build_live_activity_request(
            request,
            content_state=content_state,
            title=title,
            subtitle=subtitle,
            type=type,
            message=message,
            icon=icon,
            badge=badge,
            metrics=metrics,
            number_of_steps=number_of_steps,
            current_step=current_step,
            percentage=percentage,
            value=value,
            upper_limit=upper_limit,
            color=color,
            step_color=step_color,
            action=action,
            alert=alert,
            target=target,
            channels=channels,
        )
        return self._api.start_live_activity(
            live_activity_start_request=_normalize_channels_target(request)
        )

    def update(
        self,
        request: Any | None = None,
        *,
        activity_id: Any | None = None,
        content_state: Any | None = None,
        title: Any | None = None,
        subtitle: Any | None = None,
        type: Any | None = None,
        message: Any | None = None,
        icon: Any | None = None,
        badge: Any | None = None,
        metrics: Any | None = None,
        number_of_steps: Any | None = None,
        current_step: Any | None = None,
        percentage: Any | None = None,
        value: Any | None = None,
        upper_limit: Any | None = None,
        color: Any | None = None,
        step_color: Any | None = None,
        action: Any | None = None,
    ):
        request = _build_live_activity_request(
            request,
            activity_id=activity_id,
            content_state=content_state,
            title=title,
            subtitle=subtitle,
            type=type,
            message=message,
            icon=icon,
            badge=badge,
            metrics=metrics,
            number_of_steps=number_of_steps,
            current_step=current_step,
            percentage=percentage,
            value=value,
            upper_limit=upper_limit,
            color=color,
            step_color=step_color,
            action=action,
        )
        return self._api.update_live_activity(live_activity_update_request=request)

    def end(
        self,
        request: Any | None = None,
        *,
        activity_id: Any | None = None,
        content_state: Any | None = None,
        title: Any | None = None,
        subtitle: Any | None = None,
        type: Any | None = None,
        message: Any | None = None,
        icon: Any | None = None,
        badge: Any | None = None,
        metrics: Any | None = None,
        number_of_steps: Any | None = None,
        current_step: Any | None = None,
        percentage: Any | None = None,
        value: Any | None = None,
        upper_limit: Any | None = None,
        color: Any | None = None,
        step_color: Any | None = None,
        auto_dismiss_minutes: Any | None = None,
        action: Any | None = None,
    ):
        request = _build_live_activity_request(
            request,
            activity_id=activity_id,
            content_state=content_state,
            title=title,
            subtitle=subtitle,
            type=type,
            message=message,
            icon=icon,
            badge=badge,
            metrics=metrics,
            number_of_steps=number_of_steps,
            current_step=current_step,
            percentage=percentage,
            value=value,
            upper_limit=upper_limit,
            color=color,
            step_color=step_color,
            auto_dismiss_minutes=auto_dismiss_minutes,
            action=action,
        )
        return self._api.end_live_activity(live_activity_end_request=request)

    def stream(
        self,
        stream_key: str,
        request: Any | None = None,
        *,
        content_state: Any | None = None,
        title: Any | None = None,
        subtitle: Any | None = None,
        type: Any | None = None,
        message: Any | None = None,
        icon: Any | None = None,
        badge: Any | None = None,
        metrics: Any | None = None,
        number_of_steps: Any | None = None,
        current_step: Any | None = None,
        percentage: Any | None = None,
        value: Any | None = None,
        upper_limit: Any | None = None,
        color: Any | None = None,
        step_color: Any | None = None,
        action: Any | None = None,
        alert: Any | None = None,
        target: Any | None = None,
        channels: Any | None = None,
    ):
        request = _build_live_activity_request(
            request,
            content_state=content_state,
            title=title,
            subtitle=subtitle,
            type=type,
            message=message,
            icon=icon,
            badge=badge,
            metrics=metrics,
            number_of_steps=number_of_steps,
            current_step=current_step,
            percentage=percentage,
            value=value,
            upper_limit=upper_limit,
            color=color,
            step_color=step_color,
            action=action,
            alert=alert,
            target=target,
            channels=channels,
        )
        return self._api.reconcile_live_activity_stream(
            stream_key=stream_key,
            live_activity_stream_request=_normalize_channels_target(request),
        )

    def end_stream(
        self,
        stream_key: str,
        request: Any | None = None,
        *,
        content_state: Any | None = None,
        title: Any | None = None,
        subtitle: Any | None = None,
        type: Any | None = None,
        message: Any | None = None,
        icon: Any | None = None,
        badge: Any | None = None,
        metrics: Any | None = None,
        number_of_steps: Any | None = None,
        current_step: Any | None = None,
        percentage: Any | None = None,
        value: Any | None = None,
        upper_limit: Any | None = None,
        color: Any | None = None,
        step_color: Any | None = None,
        auto_dismiss_minutes: Any | None = None,
        action: Any | None = None,
        alert: Any | None = None,
    ):
        request = _build_live_activity_request(
            request,
            content_state=content_state,
            title=title,
            subtitle=subtitle,
            type=type,
            message=message,
            icon=icon,
            badge=badge,
            metrics=metrics,
            number_of_steps=number_of_steps,
            current_step=current_step,
            percentage=percentage,
            value=value,
            upper_limit=upper_limit,
            color=color,
            step_color=step_color,
            auto_dismiss_minutes=auto_dismiss_minutes,
            action=action,
            alert=alert,
        )
        return self._api.end_live_activity_stream(
            stream_key=stream_key,
            live_activity_stream_delete_request=request,
        )

    # Backward-compatible aliases.
    def start_live_activity(self, live_activity_start_request: Any | None = None, **kwargs: Any):
        return self.start(live_activity_start_request, **kwargs)

    def update_live_activity(self, live_activity_update_request: Any | None = None, **kwargs: Any):
        return self.update(live_activity_update_request, **kwargs)

    def end_live_activity(self, live_activity_end_request: Any | None = None, **kwargs: Any):
        return self.end(live_activity_end_request, **kwargs)

    def reconcile_live_activity_stream(
        self,
        stream_key: str,
        live_activity_stream_request: Any | None = None,
        **kwargs: Any,
    ):
        return self.stream(stream_key, live_activity_stream_request, **kwargs)

    def end_live_activity_stream(
        self,
        stream_key: str,
        live_activity_stream_delete_request: Any | None = None,
        **kwargs: Any,
    ):
        return self.end_stream(stream_key, live_activity_stream_delete_request, **kwargs)


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
