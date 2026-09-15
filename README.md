# ActivitySmith Python SDK

[Documentation](https://activitysmith.com/docs/sdks/python)

## Installation

Install the ActivitySmith Python SDK with pip:

```bash
pip install activitysmith
```

## Quickstart

1. [Create an API key](https://activitysmith.com/app/keys)
2. Set `ACTIVITYSMITH_API_KEY` or pass it directly to `ActivitySmith`.

```python
import os
from activitysmith import (
    ActivitySmith,
    action,
    alert_badge,
    alert_icon,
    content_state,
    metric,
)

activitysmith = ActivitySmith(api_key=os.environ["ACTIVITYSMITH_API_KEY"])
```

## Push Notifications

### Send a Push Notification

Send an immediate notification for a completed task or event.

![Push Notification example for a new subscription event](https://cdn.activitysmith.com/features/new-subscription-push-notification.png)

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
)
```

### Rich Push Notifications with Media

![Rich Push Notification with image](https://cdn.activitysmith.com/features/rich-push-notification-with-image.png)

```python
activitysmith.notifications.send(
    title="Homepage ready",
    message="Your agent finished the redesign.",
    media="https://cdn.example.com/output/homepage-v2.png",
)
```

Attach images, videos, or audio to your Push Notifications. Press and hold the notification to preview the media.

![Rich Push Notification with audio](https://cdn.activitysmith.com/features/rich-push-notification-with-audio.png)

What will work:

- direct image URL: `.jpg`, `.png`, `.gif`, etc.
- direct audio file URL: `.mp3`, `.m4a`, etc.
- direct video file URL: `.mp4`, `.mov`, etc.
- URL that responds with a proper media `Content-Type`, even if the path has no extension

`media` cannot be combined with `actions`.

### Push Notifications with Redirection

Open a web page, run an iOS Shortcut, or open an app when someone taps the notification. `redirection` supports:

- **HTTP/HTTPS:** Web pages, e.g. `https://example.com`
- **Shortcuts:** Run Jarvis with `shortcuts://run-shortcut?name=Jarvis` <!-- full-width -->
- **App deep links:** Installed apps or specific content within them
  - **Spotify:** A track, e.g. `spotify:track:6rqhFgbbKwnb9MLmUQDhG6`
  - **Termius:** `termius://` to open the app
  - **Claude:** `claude://code` to open the Code tab
  - **ChatGPT:** `chatgpt://` to open the app <!-- Verify ChatGPT URL scheme on iOS before publishing -->

```python
activitysmith.notifications.send(
    title="Homepage ready",
    message="Your agent finished the redesign.",
    redirection="https://github.com/acme/web/pull/482",
)
```

### Actionable Push Notifications

![Actionable Push Notification with redirection and actions](https://cdn.activitysmith.com/features/actionable-push-notifications-2.png)

`open_url` actions open a web page, run an iOS Shortcut, or open an app when someone taps the button. Supported links:

- **HTTP/HTTPS:** Web pages, e.g. `https://example.com`
- **Shortcuts:** Run Jarvis with `shortcuts://run-shortcut?name=Jarvis` <!-- full-width -->
- **App deep links:** Installed apps or specific content within them
  - **Spotify:** A track, e.g. `spotify:track:6rqhFgbbKwnb9MLmUQDhG6`
  - **Termius:** `termius://` to open the app
  - **Claude:** `claude://code` to open the Code tab
  - **ChatGPT:** `chatgpt://` to open the app <!-- Verify ChatGPT URL scheme on iOS before publishing -->

Webhooks are executed by the ActivitySmith backend and must use HTTPS.

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
    actions=[
        action(
            title="Open CRM",
            type="open_url",
            url="https://crm.example.com/customers/cus_9f3a1d",
        ),
        action(
            title="Chat with Jarvis",
            type="open_url",
            url="shortcuts://run-shortcut?name=Jarvis",
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

Choose the Live Activity type that matches what you want to show:

![Stats Live Activity with six labeled sales metrics](https://cdn.activitysmith.com/features/stats-live-activity.png)

**Stats**: Show up to 8 labeled values on your Lock Screen, from revenue and orders to uptime and conversion.

![Metrics Live Activity with CPU and memory values](https://cdn.activitysmith.com/features/metrics-live-activity-start.png)

**Metrics**: Track two related values with segmented bars, such as CPU and memory.

![Segmented Progress Live Activity showing a workflow step](https://cdn.activitysmith.com/features/update-live-activity.png)

**Segmented Progress**: Show progress through a known set of steps, like build, test, deploy, and verify.

![Progress Live Activity showing percentage completion](https://cdn.activitysmith.com/features/progress-live-activity.png)

**Progress**: Show percentage progress for jobs that move continuously toward completion.

![Alert Live Activity showing a customer reactivation update](https://cdn.activitysmith.com/features/alert-live-activity.png)

**Alert**: Show status updates with a clear message, badge, and icon. When you add an action button, `color` controls the button tint.

![Timer Live Activity showing a benchmark run countdown](https://cdn.activitysmith.com/features/timer-live-activity.png)

**Timer**: Count down from a duration, or count up from 00:00 while a job runs.

### Start & Update Live Activity

Use a stable `stream_key` to identify the metric, job, deployment, or system you want to keep visible. The first `stream(...)` call starts the Live Activity. Later calls with the same `stream_key` update it.

#### Stats

![Stats Live Activity stream example](https://cdn.activitysmith.com/features/stats-live-activity.png)

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

![Metrics Live Activity stream example](https://cdn.activitysmith.com/features/metrics-live-activity-start.png)

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

![Segmented Progress Live Activity stream example](https://cdn.activitysmith.com/features/update-live-activity.png)

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

![Progress Live Activity stream example](https://cdn.activitysmith.com/features/progress-live-activity.png)

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

#### Alert

![Alert Live Activity stream example](https://cdn.activitysmith.com/features/alert-live-activity.png)

```python
activitysmith.live_activities.stream(
    "customer-ops",
    content_state=content_state(
        title="Reactivation",
        message="Lumen came back after 2 weeks",
        type="alert",
        icon=alert_icon("cloud.sun", color="yellow"),
        badge=alert_badge("Customer", color="magenta"),
    ),
)
```

#### Timer

![Timer Live Activity stream example](https://cdn.activitysmith.com/features/timer-live-activity.png)

```python
activitysmith.live_activities.stream(
    "benchmark-run",
    content_state=content_state(
        title="Benchmark Run",
        subtitle="sampling",
        type="timer",
        duration_seconds=300,
        color="cyan",
    ),
)
```

For a countdown, send `duration_seconds`. You can update `title`, `subtitle`, `color`, or any other visible field as the work changes. Leave `duration_seconds` out unless you want to change the timer.

To start at 00:00 and count up, set `counts_down=False` and leave out `duration_seconds`.

### End Live Activity

Call `end_stream(...)` with the same `stream_key` to dismiss the Live Activity. You can include final values before it is removed. Set `auto_dismiss_seconds` to dismiss it after a delay in seconds, or `auto_dismiss_minutes` for minutes. Use `0` for immediate dismissal. Seconds take precedence if both are set.

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
        auto_dismiss_seconds=30,
    ),
)
```

### Icons and Badges

Add more context to Live Activities with icons and badges.

#### Icon

Supported Live Activity types: `stats`, `metrics`, `progress`, `segmented_progress`, `alert`, and `timer`.

![Metrics Live Activity with an SF Symbol icon on the iPhone Lock Screen](https://cdn.activitysmith.com/features/metrics-live-activity-with-icon.png)

```python
activitysmith.live_activities.stream(
    "prod-web-1",
    content_state=content_state(
        title="Server Health",
        subtitle="prod-web-1",
        type=activitysmith.live_activities.TYPE_METRICS,
        icon=alert_icon("server.rack", color="blue"),
        metrics=[
            metric(label="CPU", value=18, unit="%"),
            metric(label="MEM", value=42, unit="%"),
        ],
    ),
)
```

The `icon.symbol` value is an Apple SF Symbol name. Browse the catalog with one of these tools:

- [ActivitySmith app](https://apps.apple.com/us/app/activitysmith/id6752254835) - Open Settings -> SF Symbols to browse 45 hand-picked icons ready to use
- [SF Symbols](https://developer.apple.com/sf-symbols/) - Apple's official macOS app
- [Interactful](https://apps.apple.com/app/interactful/id1528095640) - free third-party iOS app listing all SF Symbols under Foundations -> Iconography

#### Badge

Badges are supported by `alert`, `progress`, and `segmented_progress` Live Activities.

![Progress Live Activity with a badge on the iPhone Lock Screen](https://cdn.activitysmith.com/features/progress-live-activity-with-badge.png)

```python
activitysmith.live_activities.stream(
    "nightly-database-backup",
    content_state=content_state(
        title="Nightly Database Backup",
        subtitle="verify restore",
        type=activitysmith.live_activities.TYPE_PROGRESS,
        badge=alert_badge("S3", color="cyan"),
        percentage=62,
    ),
)
```

### Live Activity Colors

Choose from these colors for the Live Activity accent, including progress bars and action buttons, or apply them to an individual icon or badge:

`lime`, `green`, `cyan`, `blue`, `purple`, `magenta`, `red`, `orange`, `yellow`, `gray`

### Live Activity Action

![Metrics Live Activity with action](https://cdn.activitysmith.com/features/metrics-live-activity-action.png)

Live Activities can include an action button.

- `open_url`: Open a web page or run an iOS Shortcut
- `webhook`: Trigger a backend GET/POST workflow

#### Open URL action

Open a web page or run an iOS Shortcut when someone taps the button. Supported links:

- **HTTP/HTTPS:** Web pages, e.g. `https://example.com`
- **Shortcuts:** Run Jarvis with `shortcuts://run-shortcut?name=Jarvis` <!-- full-width -->

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
        title="Dashboard",
        type="open_url",
        url="https://status.example.com/servers/prod-web-1",
    ),
)
```

#### Apple Shortcut action

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
        title="Chat with Jarvis",
        type="open_url",
        url="shortcuts://run-shortcut?name=Jarvis",
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

#### Secondary action

![Alert Live Activity with primary and secondary action buttons](https://cdn.activitysmith.com/features/live-activity-secondary-action.png)

Use `secondary_action` when you want a second button beside the primary `action`.

The secondary action button is supported for `alert`, `progress`, and `segmented_progress` Live Activities. Both buttons use the same `open_url`, `webhook`, and Apple Shortcut payload shapes.

```python
activitysmith.live_activities.stream(
    "agent-approval",
    content_state=content_state(
        title="Approval Needed",
        message="Should I send the follow-up email to Brightlane?",
        type="alert",
        color="green",
        icon=alert_icon("sparkles", color="green"),
        badge=alert_badge("Agent", color="green"),
    ),
    action=action(
        title="Send",
        type="webhook",
        url="https://agent.example.com/live-activity/approve",
        method="POST",
        body={
            "approval_id": "approval_01JY3J7Q9S0P8M1V5PZK7DR4M2",
            "decision": "send",
        },
    ),
    secondary_action=action(
        title="Deny",
        type="webhook",
        url="https://agent.example.com/live-activity/deny",
        method="POST",
        body={
            "approval_id": "approval_01JY3J7Q9S0P8M1V5PZK7DR4M2",
            "decision": "deny",
        },
    ),
)
```

## Lock Screen Widgets

![Lock screen widgets](https://cdn.activitysmith.com/features/lock-screen-widgets.png)

ActivitySmith lets you display any value on your Lock Screen with widgets - SaaS metrics, revenue, signups, uptime, habits, or anything else you want to track. Create a metric in the [web app](https://activitysmith.com/app/widgets), then update the metric value using our API, add a widget to your lock screen and it will fetch the latest update automatically.

![Create widget metric](https://cdn.activitysmith.com/features/create-widget-metric.png)

Use the metric key to update its value.

```python
activitysmith.metrics.update("deploy.success_rate", 99.9)
```

String metric values work too.

```python
activitysmith.metrics.update("prod.status", "healthy")
```

## App Icon Badge Count

![ActivitySmith app icon with an App Icon Badge Count](https://cdn.activitysmith.com/features/badge-count.png)

Show the number you care about on your ActivitySmith app icon. Track MRR, a customer count, a stock price, or any other value you want to keep in view.

### Set or update the badge value

```python
activitysmith.badge_count(8333)
```

### Clear the badge

Pass `0` to clear the badge.

```python
activitysmith.badge_count(0)
```

## Metadata

Metadata adds extra information to Push Notification and Live Activity details in ActivitySmith. It does not appear in the notification or Live Activity on your device.

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
    metadata={
        "customer_id": "382",
        "plan": "Pro",
        "amount": 29,
        "trial": False,
    },
)

activitysmith.live_activities.stream(
    "customer-import",
    title="Customer Import",
    type="progress",
    percentage=60,
    metadata={
        "job_id": "import-382",
        "records": 1200,
    },
)
```

Values can be strings, numbers, or booleans. Metadata supports up to 50 entries and 16 KB of JSON, with keys up to 100 characters and strings up to 4,000 characters. Nested objects, arrays, and null values are not supported.

## Tags

Use Tags to organize and filter Push Notification and Live Activity history. Tags are created automatically when you first use them. Sending Tags requires SDK version 1.10.0 or later.

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
    tags=["user:382", "billing"],
)
```

On Live Activity stream updates and legacy `update` or `end` calls, omit `tags` to keep existing Tags, supply a list to replace them, or pass `tags=[]` to clear them.

```python
activitysmith.live_activities.update(
    activity_id="YOUR_ACTIVITY_ID",
    title="Customer Import",
    percentage=60,
    tags=[],
)
```

## Channels

Use `channels` to target specific team members or devices when sending Push Notifications, Live Activities, or App Icon Badge Count updates. Omit it for account-wide delivery.

```python
activitysmith.notifications.send(
    title="New subscription 💸",
    message="Customer upgraded to Pro plan",
    channels=["sales", "customer-success"],
)

activitysmith.live_activities.stream(
    "nightly-backup",
    content_state=content_state(
        title="Nightly database backup",
        type="segmented_progress",
        number_of_steps=3,
        current_step=1,
    ),
    channels=["ios-builds"],
)

activitysmith.badge_count(3, channels=["sales", "customer-success"])
```

## Error Handling

Wrap API calls with `try/except`. The SDK raises exceptions for non-2xx responses. Rate limit errors use the `error` and `message` fields, and Live Activity limit errors include `limit` and `active`. See [Rate Limits](https://activitysmith.com/docs/rate-limits) for details.

## Additional Resources

### [PyPI Package](https://pypi.org/project/activitysmith/)

Install the ActivitySmith Python SDK from PyPI
