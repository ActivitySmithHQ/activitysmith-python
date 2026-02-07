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

```python
response = activitysmith.notifications.send(
    {
        "title": "Build Failed",
        "message": "CI pipeline failed on main branch",
    }
)

print(response.success)
print(response.devices_notified)
```

### Start a Live Activity

```python
start = activitysmith.live_activities.start(
    {
        "content_state": {
            "title": "ActivitySmith API Deployment",
            "subtitle": "start",
            "number_of_steps": 4,
            "current_step": 1,
            "type": "segmented_progress",
            "color": "yellow",
        }
    }
)

activity_id = start.activity_id
```

### Update a Live Activity

```python
update = activitysmith.live_activities.update(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "ActivitySmith API Deployment",
            "subtitle": "npm i & pm2",
            "current_step": 3,
        }
    }
)

print(update.devices_notified)
```

### End a Live Activity

```python
end = activitysmith.live_activities.end(
    {
        "activity_id": activity_id,
        "content_state": {
            "title": "ActivitySmith API Deployment",
            "subtitle": "done",
            "current_step": 4,
            "auto_dismiss_minutes": 3,
        }
    }
)

print(end.success)
```

## Error Handling

```python
try:
    activitysmith.notifications.send(
        {
            "title": "Build Failed",
        }
    )
except Exception as err:
    print("Request failed:", err)
```

## API Surface

- `activitysmith.live_activities`
- `activitysmith.notifications`

Request/response models are included and can be imported from `activitysmith_openapi.models`.

## Requirements

- Python 3.9 or newer

## License

MIT
