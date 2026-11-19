# StreamContentState

Current state for a managed Live Activity stream. Include type on the first PUT, and whenever the stream may need to start a fresh activity. Supports segmented_progress, progress, metrics, stats, alert, timer, and value types. For timer, send duration_seconds or timer_end_at to start or reset a bounded timer, and timer_start_at for a timer that started earlier. Omit them on later updates to preserve the existing timer window.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Title shown on the Live Activity. Send an empty string to show no title. | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Use for segmented_progress. | [optional] 
**current_step** | **int** | Use for segmented_progress. Set 0 when no segment is complete yet. Must be less than or equal to number_of_steps when number_of_steps is provided. | [optional] 
**percentage** | **float** | Use for progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | [**LiveActivityValue**](LiveActivityValue.md) | For type&#x3D;value, the required prominent readout (string or finite number); strings preserve exact formatting. For progress, a numeric progress value used with upper_limit. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for progress. | [optional] 
**duration_seconds** | **float** | Timer duration in seconds. For type&#x3D;timer, send duration_seconds to start or reset the timer window, counted from timer_start_at when you send it. Omit it on later stream updates to preserve the existing timer window. | [optional] 
**timer_start_at** | **datetime** | Use with type&#x3D;timer. ISO 8601 date and time when the timer started. It can be in the past, so a countdown that started earlier shows the time already gone in its progress bar. Defaults to the request time. Must not be in the future. | [optional] 
**timer_end_at** | **datetime** | Use with type&#x3D;timer. ISO 8601 date and time when the countdown ends. Must be after timer_start_at, or in the future when timer_start_at is omitted. Send duration_seconds or timer_end_at, not both. On later stream updates, send timer_end_at alone to move the end and keep the current start. | [optional] 
**counts_down** | **bool** | Use with type&#x3D;timer. When true or omitted, the timer counts down from duration_seconds. Set false for an elapsed timer; omit duration_seconds for an open-ended elapsed timer. | [optional] [default to True]
**is_running** | **bool** | Use with type&#x3D;timer. Defaults to true. Set false to pause/freeze via API; set true on a paused timer to resume. | [optional] [default to True]
**type** | **str** | Required on the first PUT or whenever the stream cannot infer the current activity type. | [optional] 
**color** | **str** | Optional. Accent color for progress, segmented_progress, metrics, timer, and value Live Activities. For Alert Live Activities, this tints action and secondary_action buttons when included. | [optional] 
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to segmented_progress. | [optional] 
**step_colors** | **List[str]** | Optional. Colors for completed steps. When used with segmented_progress, the array length should match current_step. | [optional] 
**metrics** | [**List[ActivityMetric]**](ActivityMetric.md) | Use for metrics and stats activities. | [optional] 
**message** | **str** | Required for type&#x3D;alert. | [optional] 
**icon** | [**LiveActivityAlertIcon**](LiveActivityAlertIcon.md) | Optional SF Symbol icon. Supported by alert, progress, segmented_progress, metrics, stats, timer, and value. | [optional] 
**badge** | [**LiveActivityAlertBadge**](LiveActivityAlertBadge.md) | Optional badge. Supported by alert, progress, segmented_progress, and value. | [optional] 
**auto_dismiss_seconds** | **int** | Optional. Seconds before the ended Live Activity is dismissed. | [optional] 
**auto_dismiss_minutes** | **int** | Optional. Minutes before the ended Live Activity is dismissed. | [optional] 

## Example

```python
from activitysmith_openapi.models.stream_content_state import StreamContentState

# TODO update the JSON string below
json = "{}"
# create an instance of StreamContentState from a JSON string
stream_content_state_instance = StreamContentState.from_json(json)
# print the JSON string representation of the object
print(StreamContentState.to_json())

# convert the object into a dict
stream_content_state_dict = stream_content_state_instance.to_dict()
# create an instance of StreamContentState from a dict
stream_content_state_from_dict = StreamContentState.from_dict(stream_content_state_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


