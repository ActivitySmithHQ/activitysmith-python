# StreamContentState

Current state for a managed Live Activity stream. Include type on the first PUT, and whenever the stream may need to start a fresh activity. Supports segmented_progress, progress, metrics, and the legacy counter/timer/countdown step-based types.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Use for segmented_progress, counter, timer, and countdown. | [optional] 
**current_step** | **int** | Use for segmented_progress, counter, timer, and countdown. | [optional] 
**percentage** | **float** | Use for progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for progress. | [optional] 
**type** | **str** | Required on the first PUT or whenever the stream cannot infer the current activity type. | [optional] 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to segmented_progress. | [optional] 
**step_colors** | **List[str]** | Optional. Colors for completed steps. When used with segmented_progress, the array length should match current_step. | [optional] 
**metrics** | [**List[ActivityMetric]**](ActivityMetric.md) | Use for metrics activities. | [optional] 
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


