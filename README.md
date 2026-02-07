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

## Usage

```python
import os
from activitysmith import ActivitySmith

activitysmith = ActivitySmith(
    api_key=os.environ["ACTIVITYSMITH_API_KEY"],
)

# Push Notifications
activitysmith.notifications.send(
    {
        # See PushNotificationRequest for fields
    }
)

# Live Activities
activitysmith.live_activities.start(
    {
        # See LiveActivityStartRequest for fields
    }
)
```

## API Surface

The client exposes grouped resources:

- `activitysmith.live_activities`
- `activitysmith.notifications`

Request/response models are included and can be imported from `activitysmith_openapi.models`.

## Requirements

- Python 3.9 or newer

## License

MIT
