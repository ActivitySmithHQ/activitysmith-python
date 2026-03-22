# ActivitySmith Python Library

The ActivitySmith Python library provides convenient access to the ActivitySmith API from Python applications.

## Documentation

See the [API reference](https://activitysmith.com/docs/api-reference/introduction).

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
from activitysmith import ActivitySmith

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
    {
        "title": "New subscription 💸",
        "message": "Customer upgraded to Pro plan",
    }
)
```

### Rich Push Notifications with Media

<p align="center">
  <img src="https://cdn.activitysmith.com/features/rich-push-notification-with-image.png" alt="Rich push notification with image" width="680" />
</p>

```python
activitysmith.notifications.send(
    {
        "title": "Homepage ready",
        "message": "Your agent finished the redesign.",
        "media": "https://cdn.example.com/output/homepage-v2.png",
        "redirection": "https://github.com/acme/web/pull/482",
    }
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
    {
        "title": "New subscription 💸",
        "message": "Customer upgraded to Pro plan",
        "redirection": "https://crm.example.com/customers/cus_9f3a1d",  # Optional
        "actions": [  # Optional (max 4)
            {
                "title": "Open CRM Profile",
                "type": "open_url",
                "url": "https://crm.example.com/customers/cus_9f3a1d",
            },
            {
                "title": "Start Onboarding Workflow",
                "type": "webhook",
                "url": "https://hooks.example.com/activitysmith/onboarding/start",
                "method": "POST",
                "body": {
                    "customer_id": "cus_9f3a1d",
                    "plan": "pro",
                },
            },
        ],
    }
)
```

## Live Activities

<p align="center">
  <img src="https://cdn.activitysmith.com/features/metrics-live-activity-action.png" alt="Live Activities example" width="680" />
</p>

ActivitySmith supports two ways to drive Live Activities:

- Recommended: stream updates with `activitysmith.live_activities.stream(...)`
- Advanced: manual lifecycle control with `start`, `update`, and `end`

Use stream updates when you want the easiest, stateless flow. You don't need to
store `activity_id` or manage lifecycle state yourself. Send the latest state
for a stable `stream_key` and ActivitySmith will start or update the Live
Activity for you. When the tracked process is over, call `end_stream(...)`.

Use the manual lifecycle methods when you need direct control over a specific
Live Activity instance.

Live Activity UI types:

- `metrics`: best for live operational stats like server CPU and memory, queue depth, or replica lag
- `segmented_progress`: best for step-based workflows like deployments, backups, and ETL pipelines
- `progress`: best for continuous jobs like uploads, reindexes, and long-running migrations tracked as a percentage

### Recommended: Stream updates

Use a stable `stream_key` to identify the system or workflow you are tracking,
such as a server, deployment, build pipeline, cron job, or charging session.
This is especially useful for cron jobs and other scheduled tasks where you do
not want to store `activity_id` between runs.

#### Metrics

<p align="center">
  <img src="https://cdn.activitysmith.com/features/metrics-live-activity-start.png" alt="Metrics stream example" width="680" />
</p>

```python
status = activitysmith.live_activities.stream(
    "prod-web-1",
    {
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 9, "unit": "%"},
                {"label": "MEM", "value": 45, "unit": "%"},
            ],
        },
    },
)
```

#### Segmented progress

<p align="center">
  <img src="https://cdn.activitysmith.com/features/update-live-activity.png" alt="Segmented progress stream example" width="680" />
</p>

```python
activitysmith.live_activities.stream(
    "nightly-backup",
    {
        "content_state": {
            "title": "Nightly Backup",
            "subtitle": "upload archive",
            "type": "segmented_progress",
            "number_of_steps": 3,
            "current_step": 2,
        },
    },
)
```

#### Progress

<p align="center">
  <img src="https://cdn.activitysmith.com/features/progress-live-activity.png" alt="Progress stream example" width="680" />
</p>

```python
activitysmith.live_activities.stream(
    "search-reindex",
    {
        "content_state": {
            "title": "Search Reindex",
            "subtitle": "catalog-v2",
            "type": "progress",
            "percentage": 42,
        },
    },
)
```

Call `stream(...)` again with the same `stream_key` whenever the state changes.

#### End a stream

Use this when the tracked process is finished and you no longer want the Live
Activity on devices. `content_state` is optional here; include it if you want
to end the stream with a final state.

```python
activitysmith.live_activities.end_stream(
    "prod-web-1",
    {
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 7, "unit": "%"},
                {"label": "MEM", "value": 38, "unit": "%"},
            ],
        },
    },
)
```

If you later send another `stream(...)` request with the same `stream_key`,
ActivitySmith starts a new Live Activity for that stream again.

Stream responses include an `operation` field:

- `started`: ActivitySmith started a new Live Activity for this `stream_key`
- `updated`: ActivitySmith updated the current Live Activity
- `rotated`: ActivitySmith ended the previous Live Activity and started a new one
- `noop`: the incoming state matched the current state, so no update was sent
- `paused`: the stream is paused, so no Live Activity was started or updated
- `ended`: returned by `end_stream(...)` after the stream is ended

### Advanced: Manual lifecycle control

Use these methods when you want to manage the Live Activity lifecycle yourself.

#### Shared flow

1. Call `activitysmith.live_activities.start(...)`.
2. Save the returned `activity_id`.
3. Call `activitysmith.live_activities.update(...)` as progress changes.
4. Call `activitysmith.live_activities.end(...)` when the work is finished.

### Metrics Type

Use `metrics` when you want to keep a small set of live stats visible, such as
server health, queue pressure, or database load.

#### Start

<p align="center">
  <img src="https://cdn.activitysmith.com/features/metrics-live-activity-start.png" alt="Metrics start example" width="680" />
</p>

```python
start = activitysmith.live_activities.start(
    {
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 9, "unit": "%"},
                {"label": "MEM", "value": 45, "unit": "%"},
            ],
        },
    }
)

activity_id = start.activity_id
```

#### Update

<p align="center">
  <img src="https://cdn.activitysmith.com/features/metrics-live-activity-update.png" alt="Metrics update example" width="680" />
</p>

```python
activitysmith.live_activities.update(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 76, "unit": "%"},
                {"label": "MEM", "value": 52, "unit": "%"},
            ],
        },
    }
)
```

#### End

<p align="center">
  <img src="https://cdn.activitysmith.com/features/metrics-live-activity-end.png" alt="Metrics end example" width="680" />
</p>

```python
activitysmith.live_activities.end(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 7, "unit": "%"},
                {"label": "MEM", "value": 38, "unit": "%"},
            ],
            "auto_dismiss_minutes": 2,
        },
    }
)
```

### Segmented Progress Type

Use `segmented_progress` when progress is easier to follow as steps instead of a
raw percentage. It fits jobs like backups, deployments, ETL pipelines, and
checklists where "step 2 of 3" is more useful than "67%". `number_of_steps` is
dynamic, so you can increase or decrease it later if the workflow changes.

#### Start

<p align="center">
  <img src="https://cdn.activitysmith.com/features/start-live-activity.png" alt="Segmented progress start example" width="680" />
</p>

```python
start = activitysmith.live_activities.start(
    {
        "content_state": {
            "title": "Nightly database backup",
            "subtitle": "create snapshot",
            "number_of_steps": 3,
            "current_step": 1,
            "type": "segmented_progress",
            "color": "yellow",
        },
    }
)

activity_id = start.activity_id
```

#### Update

<p align="center">
  <img src="https://cdn.activitysmith.com/features/update-live-activity.png" alt="Segmented progress update example" width="680" />
</p>

```python
activitysmith.live_activities.update(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Nightly database backup",
            "subtitle": "upload archive",
            "number_of_steps": 3,
            "current_step": 2,
        },
    }
)
```

#### End

<p align="center">
  <img src="https://cdn.activitysmith.com/features/end-live-activity.png" alt="Segmented progress end example" width="680" />
</p>

```python
activitysmith.live_activities.end(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Nightly database backup",
            "subtitle": "verify restore",
            "number_of_steps": 3,
            "current_step": 3,
            "auto_dismiss_minutes": 2,
        },
    }
)
```

### Progress Type

Use `progress` when the state is naturally continuous. It fits charging,
downloads, sync jobs, uploads, timers, and any flow where a percentage or
numeric range is the clearest signal.

#### Start

<p align="center">
  <img src="https://cdn.activitysmith.com/features/progress-live-activity-start.png" alt="Progress start example" width="680" />
</p>

```python
start = activitysmith.live_activities.start(
    {
        "content_state": {
            "title": "EV Charging",
            "subtitle": "Added 30 mi range",
            "type": "progress",
            "percentage": 15,
        }
    }
)

activity_id = start.activity_id
```

#### Update

<p align="center">
  <img src="https://cdn.activitysmith.com/features/progress-live-activity-update.png" alt="Progress update example" width="680" />
</p>

```python
activitysmith.live_activities.update(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "EV Charging",
            "subtitle": "Added 120 mi range",
            "percentage": 60,
        }
    }
)
```

#### End

<p align="center">
  <img src="https://cdn.activitysmith.com/features/progress-live-activity-end.png" alt="Progress end example" width="680" />
</p>

```python
activitysmith.live_activities.end(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "EV Charging",
            "subtitle": "Added 200 mi range",
            "percentage": 100,
            "auto_dismiss_minutes": 2,
        }
    }
)
```

### Live Activity Action

Just like Actionable Push Notifications, Live Activities can have a button that opens a URL in a browser or triggers a webhook. Webhooks are executed by the ActivitySmith backend.

<p align="center">
  <img src="https://cdn.activitysmith.com/features/metrics-live-activity-action.png" alt="Metrics Live Activity with action" width="680" />
</p>

#### Open URL action

```python
start = activitysmith.live_activities.start(
    {
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 76, "unit": "%"},
                {"label": "MEM", "value": 52, "unit": "%"},
            ],
        },
        "action": {
            "title": "Open Dashboard",
            "type": "open_url",
            "url": "https://ops.example.com/servers/prod-web-1",
        },
    }
)

activity_id = start.activity_id
```

#### Webhook action

```python
activitysmith.live_activities.update(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Server Health",
            "subtitle": "prod-web-1",
            "type": "metrics",
            "metrics": [
                {"label": "CPU", "value": 91, "unit": "%"},
                {"label": "MEM", "value": 57, "unit": "%"},
            ],
        },
        "action": {
            "title": "Restart Service",
            "type": "webhook",
            "url": "https://ops.example.com/hooks/servers/prod-web-1/restart",
            "method": "POST",
            "body": {
                "server_id": "prod-web-1",
                "requested_by": "activitysmith-python",
            },
        },
    }
)
```

## Channels

Channels are used to target specific team members or devices. Can be used for both push notifications and live activities.

```python
activitysmith.notifications.send(
    {
        "title": "New subscription 💸",
        "message": "Customer upgraded to Pro plan",
        "channels": ["sales", "customer-success"],  # Optional
    }
)
```

## Error Handling

```python
try:
    activitysmith.notifications.send(
        {
            "title": "New subscription 💸",
        }
    )
except Exception as err:
    print("Request failed:", err)
```

Request/response models are included and can be imported from `activitysmith_openapi.models`.

## Requirements

- Python 3.9 or newer

## License

MIT
