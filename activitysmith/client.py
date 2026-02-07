from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from activitysmith_openapi.configuration import Configuration
from activitysmith_openapi.api_client import ApiClient

from activitysmith_openapi.api.live_activities_api import LiveActivitiesApi
from activitysmith_openapi.api.push_notifications_api import PushNotificationsApi


class NotificationsResource:
    def __init__(self, api: PushNotificationsApi) -> None:
        self._api = api

    def send(self, request: Any):
        return self._api.send_push_notification(push_notification_request=request)

    # Backward-compatible alias.
    def send_push_notification(self, push_notification_request: Any):
        return self.send(push_notification_request)


class LiveActivitiesResource:
    def __init__(self, api: LiveActivitiesApi) -> None:
        self._api = api

    def start(self, request: Any):
        return self._api.start_live_activity(live_activity_start_request=request)

    def update(self, request: Any):
        return self._api.update_live_activity(live_activity_update_request=request)

    def end(self, request: Any):
        return self._api.end_live_activity(live_activity_end_request=request)

    # Backward-compatible aliases.
    def start_live_activity(self, live_activity_start_request: Any):
        return self.start(live_activity_start_request)

    def update_live_activity(self, live_activity_update_request: Any):
        return self.update(live_activity_update_request)

    def end_live_activity(self, live_activity_end_request: Any):
        return self.end(live_activity_end_request)


@dataclass
class ActivitySmith:
    api_key: str

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("ActivitySmith: api_key is required")

        config = Configuration(access_token=self.api_key)

        api_client = ApiClient(configuration=config)

        self.notifications = NotificationsResource(PushNotificationsApi(api_client))
        self.live_activities = LiveActivitiesResource(LiveActivitiesApi(api_client))
