# ActivitySmith Python Library

The ActivitySmith Python library provides convenient access to the ActivitySmith API from Python applications.

## Documentation

See the [API reference](https://activitysmith.com/docs/api-reference/introduction).

## Table of Contents

- [Installation](#installation)
- [Setup](#setup)
- [Push Notifications](#push-notifications)
  - [Send a Push Notification](#send-a-push-notification)
  - [Rich Push Notifications with Media](#rich-push-notifications-with-media)
  - [Actionable Push Notifications](#actionable-push-notifications)
- [Live Activities](#live-activities)
  - [Start & Update Live Activity](#start--update-live-activity)
  - [End Live Activity](#end-live-activity)
  - [Live Activity Action](#live-activity-action)
- [Channels](#channels)
- [Widgets](#widgets)

## Installation

This package is available on PyPI:

```sh
pip install activitysmith
```

Alternatively, install from source with:

```sh
python -m pip install .
```

## Setup

```python
import os
from activitysmith import ActivitySmith, action, content_state, metric

activitysmith = ActivitySmith(
    api_key=os.environ["ACTIVITYSMITH_API_KEY"],
)
```

## Push Notifications

### Send a Push Notification

<p align="center">
  <img src="https://cdn.activitysmith.com/features/new-subscription-push-notification.png" alt="Push notification example" width="680" />
</p>

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
)
```

### Rich Push Notifications with Media

<p align="center">
  <img src="https://cdn.activitysmith.com/features/rich-push-notification-with-image.png" alt="Rich push notification with image" width="680" />
</p>

```python
activitysmith.notifications.send(
    title="Homepage ready",
    message="Your agent finished the redesign.",
    media="https://cdn.example.com/output/homepage-v2.png",
    redirection="https://github.com/acme/web/pull/482",
)
```

Send images, videos, or audio with your push notifications, press and hold to preview media directly from the notification, then tap through to open the linked content.

<p align="center">
  <img src="https://cdn.activitysmith.com/features/rich-push-notification-with-audio.png" alt="Rich push notification with audio" width="680" />
</p>

What will work:

- direct image URL: `.jpg`, `.png`, `.gif`, etc.
- direct audio file URL: `.mp3`, `.m4a`, etc.
- direct video file URL: `.mp4`, `.mov`, etc.
- URL that responds with a proper media `Content-Type`, even if the path has no extension

### Actionable Push Notifications

<p align="center">
  <img src="https://cdn.activitysmith.com/features/actionable-push-notifications-2.png" alt="Actionable push notification example" width="680" />
</p>

Actionable push notifications can open a URL on tap or trigger actions when someone long-presses the notification.
Webhooks are executed by the ActivitySmith backend.

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
    redirection="https://crm.example.com/customers/cus_9f3a1d",  # Optional
    actions=[  # Optional (max 4)
        action(
            title="Open CRM Profile",
            type="open_url",
            url="https://crm.example.com/customers/cus_9f3a1d",
        ),
        action(
            title="Start Onboarding Workflow",
            type="webhook",
            url="https://hooks.example.com/activitysmith/onboarding/start",
            method="POST",
            body={
                "customer_id": "cus_9f3a1d",
                "plan": "pro",
            },
        ),
    ],
)
```

## Live Activities

There are four types of Live Activities:

- `stats`: best for showing business numbers side by side, such as revenue, sales, new users, conversion, refunds, or any other value you want visible at a glance
- `metrics`: best for live percentage values that change often, like server CPU, memory usage, disk usage, or error rate
- `segmented_progress`: best for anything that moves through clear stages, like deployments, onboarding flows, backups, ETL pipelines, migrations, and AI agent runs
- `progress`: best for tracking real-time progress with percentage, like tasks, backups, migrations, syncs, or uploads

### Start & Update Live Activity

Use a stable `stream_key` to identify the metric, job, deployment, or system you want to keep visible. The first `stream(...)` call starts the Live Activity. Later calls with the same `stream_key` update it.

#### Stats

<p align="center">
  <img
    src="https://cdn.activitysmith.com/features/stats-live-activity.png"
    alt="Stats Live Activity stream example"
    width="680"
  />
</p>

```python
activitysmith.live_activities.stream(
    "sales-hourly",
    content_state=content_state(
        title="Sales",
        subtitle="last hour",
        type="stats",
        metrics=[
            metric(label="Revenue", value="$2430", color="blue"),
            metric(label="Orders", value="37", color="green"),
            metric(label="Conversion", value="4.8%", color="magenta"),
            metric(label="Avg Order", value="$65.68", color="yellow"),
            metric(label="Refunds", value="$84", color="red"),
            metric(label="New Buyers", value="18", color="cyan"),
        ],
    ),
)
```

#### Metrics

<p align="center">
  <img
    src="https://cdn.activitysmith.com/features/metrics-live-activity-start.png"
    alt="Metrics Live Activity stream example"
    width="680"
  />
</p>

```python
activitysmith.live_activities.stream(
    "prod-web-1",
    content_state=content_state(
        title="Server Health",
        subtitle="prod-web-1",
        type="metrics",
        metrics=[
            metric(label="CPU", value=9, unit="%"),
            metric(label="MEM", value=45, unit="%"),
        ],
    ),
)
```

#### Segmented Progress

<p align="center">
  <img
    src="https://cdn.activitysmith.com/features/update-live-activity.png"
    alt="Segmented Progress Live Activity stream example"
    width="680"
  />
</p>

```python
activitysmith.live_activities.stream(
    "nightly-backup",
    content_state=content_state(
        title="Nightly Backup",
        subtitle="upload archive",
        type="segmented_progress",
        number_of_steps=3,
        current_step=2,
    ),
)
```

#### Progress

<p align="center">
  <img
    src="https://cdn.activitysmith.com/features/progress-live-activity.png"
    alt="Progress Live Activity stream example"
    width="680"
  />
</p>

```python
activitysmith.live_activities.stream(
    "search-reindex",
    content_state=content_state(
        title="Search Reindex",
        subtitle="catalog-v2",
        type="progress",
        percentage=42,
    ),
)
```

### End Live Activity

Call `end_stream(...)` with the same `stream_key` to dismiss the Live Activity. You can include final values before it is removed. By default, iOS removes the Live Activity after two minutes. Set `auto_dismiss_minutes` to choose a different dismissal time, including `0` for immediate dismissal.

```python
activitysmith.live_activities.end_stream(
    "prod-web-1",
    content_state=content_state(
        title="Server Health",
        subtitle="prod-web-1",
        type="metrics",
        metrics=[
            metric(label="CPU", value=7, unit="%"),
            metric(label="MEM", value=38, unit="%"),
        ],
        auto_dismiss_minutes=2,
    ),
)
```

### Live Activity Action

Live Activities can include one optional action button. Use it to open a URL from the Live Activity or trigger a backend webhook.

<p align="center">
  <img
    src="https://cdn.activitysmith.com/features/live-activity-with-action.png?v=20260319-1"
    alt="Live Activity with action button"
    width="680"
  />
</p>

#### Open URL action

```python
activitysmith.live_activities.stream(
    "prod-web-1",
    content_state=content_state(
        title="Server Health",
        subtitle="prod-web-1",
        type="metrics",
        metrics=[
            metric(label="CPU", value=76, unit="%"),
            metric(label="MEM", value=52, unit="%"),
        ],
    ),
    action=action(
        title="Open Dashboard",
        type="open_url",
        url="https://ops.example.com/servers/prod-web-1",
    ),
)
```

#### Webhook action

```python
activitysmith.live_activities.stream(
    "search-reindex",
    content_state=content_state(
        title="Reindexing product search",
        subtitle="Shard 7 of 12",
        type="segmented_progress",
        number_of_steps=12,
        current_step=7,
    ),
    action=action(
        title="Pause Reindex",
        type="webhook",
        url="https://ops.example.com/hooks/search/reindex/pause",
        method="POST",
        body={
            "job_id": "reindex-2026-03-19",
            "requested_by": "activitysmith-python",
        },
    ),
)
```

## Channels

Channels are used to target specific team members or devices. Can be used for both push notifications and live activities.

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
    channels=["sales", "customer-success"],  # Optional
)
```

## Widgets

<p align="center">
  <img src="https://cdn.activitysmith.com/features/lock-screen-widgets.png" alt="Lock screen widgets" width="680" />
</p>

ActivitySmith lets you display any value on your Lock Screen with widgets - SaaS metrics, revenue, signups, uptime, habits, or anything else you want to track. Create a metric in the <a href="https://activitysmith.com/app/widgets" target="_blank" rel="noopener noreferrer">web app</a>, then update the metric value using our API, add a widget to your lock screen and it will fetch the latest update automatically.

<p align="center">
  <img src="https://cdn.activitysmith.com/features/create-widget-metric.png" alt="Create widget metric" width="680" />
</p>

```python
activitysmith.metrics.update("deploy.success_rate", 99.9)
```

String metric values work too.

```python
activitysmith.metrics.update("prod.status", "healthy")
```

## Error Handling

```python
try:
    activitysmith.notifications.send(
        title="New subscription 💸",
    )
except Exception as err:
    print("Request failed:", err)
```

Request/response models are included and can be imported from `activitysmith_openapi.models`.

## Requirements

- Python 3.9 or newer

## License

MIT
