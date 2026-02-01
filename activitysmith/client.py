from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from activitysmith_openapi.configuration import Configuration
from activitysmith_openapi.api_client import ApiClient

from activitysmith_openapi.api.live_activities_api import LiveActivitiesApi
from activitysmith_openapi.api.push_notifications_api import PushNotificationsApi


@dataclass
class ActivitySmith:
    api_key: str
    base_url: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.api_key:
            raise ValueError("ActivitySmith: api_key is required")

        config = Configuration(access_token=self.api_key)
        if self.base_url:
            config.host = self.base_url

        api_client = ApiClient(configuration=config)

        self.notifications = PushNotificationsApi(api_client)
        self.live_activities = LiveActivitiesApi(api_client)