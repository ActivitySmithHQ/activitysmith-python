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

## Usage

### Send a Push Notification

<p align="center">
  <img src="https://cdn.activitysmith.com/features/new-subscription-push-notification.png" alt="Push notification example" width="680" />
</p>

```python
response = activitysmith.notifications.send(
    {
        "title": "New subscription 💸",
        "message": "Customer upgraded to Pro plan",
    }
)

print(response.success)
print(response.devices_notified)
```

## Live Activities

Live Activities come in two UI types, but the lifecycle stays the same:
start the activity, keep the returned `activity_id`, update it as state
changes, then end it when the work is done.

- `segmented_progress`: best for jobs tracked in steps
- `progress`: best for jobs tracked as a percentage or numeric range

### Shared flow

1. Call `activitysmith.live_activities.start(...)`.
2. Save the returned `activity_id`.
3. Call `activitysmith.live_activities.update(...)` as progress changes.
4. Call `activitysmith.live_activities.end(...)` when the work is finished.

### Segmented Progress Type

Use `segmented_progress` when progress is easier to follow as steps instead of a
raw percentage. It fits jobs like backups, deployments, ETL pipelines, and
checklists where "step 2 of 3" is more useful than "67%".
`number_of_steps` is dynamic, so you can increase or decrease it later if the
workflow changes.

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
        "channels": ["devs", "ops"],  # Optional
    }
)

activity_id = start.activity_id
```

#### Update

<p align="center">
  <img src="https://cdn.activitysmith.com/features/update-live-activity.png" alt="Segmented progress update example" width="680" />
</p>

```python
update = activitysmith.live_activities.update(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Nightly database backup",
            "subtitle": "upload archive",
            "number_of_steps": 4,
            "current_step": 2,
        }
    }
)

print(update.devices_notified)
```

#### End

<p align="center">
  <img src="https://cdn.activitysmith.com/features/end-live-activity.png" alt="Segmented progress end example" width="680" />
</p>

```python
end = activitysmith.live_activities.end(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "Nightly database backup",
            "subtitle": "verify restore",
            "number_of_steps": 4,
            "current_step": 4,
            "auto_dismiss_minutes": 2,
        }
    }
)

print(end.success)
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
            "color": "lime",
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

## Channels

Channels are used to target specific team members or devices. Can be used for both push notifications and live activities.

```python
response = activitysmith.notifications.send(
    {
        "title": "New subscription 💸",
        "message": "Customer upgraded to Pro plan",
        "channels": ["sales", "customer-success"],  # Optional
    }
)
```

## Push Notification Redirection and Actions

Push notification redirection and actions are optional and can be used to redirect the user to a specific URL when they tap the notification or to trigger a specific action when they long-press the notification.
Webhooks are executed by ActivitySmith backend.

```python
response = activitysmith.notifications.send(
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
