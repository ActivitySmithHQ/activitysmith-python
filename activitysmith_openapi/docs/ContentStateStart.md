# ContentStateStart

Start payload requires title and type. For segmented_progress include number_of_steps and current_step. For progress include percentage or value with upper_limit. For metrics and stats include a non-empty metrics array. For alert include message. For timer include duration_seconds for countdowns, or set counts_down false without duration_seconds for an open-ended elapsed timer. Optional icon is supported by all Live Activity types. Optional badge is supported by alert, progress, and segmented_progress. For segmented_progress, number_of_steps is not locked and can be changed in later update or end calls.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Total number of steps. Use for type&#x3D;segmented_progress. This value can be increased or decreased later when updating or ending the same activity. | [optional] 
**current_step** | **int** | Current completed step count. Use for type&#x3D;segmented_progress. Set 0 when the activity has started but no segment is complete yet. Must be less than or equal to number_of_steps. | [optional] 
**percentage** | **float** | Progress percentage (0–100). Use for type&#x3D;progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for type&#x3D;progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for type&#x3D;progress. | [optional] 
**duration_seconds** | **float** | Timer duration in seconds. For type&#x3D;timer countdowns, required on start when counts_down is true or omitted. | [optional] 
**counts_down** | **bool** | Use with type&#x3D;timer. When true or omitted, the timer counts down from duration_seconds. Set false for an elapsed timer; omit duration_seconds for an open-ended elapsed timer. | [optional] [default to True]
**is_running** | **bool** | Use with type&#x3D;timer. Defaults to true. Set false to pause/freeze via API; set true on a paused timer to resume. | [optional] [default to True]
**metrics** | [**List[ActivityMetric]**](ActivityMetric.md) | Use for type&#x3D;metrics or type&#x3D;stats. | [optional] 
**message** | **str** | Required for type&#x3D;alert. | [optional] 
**icon** | [**LiveActivityAlertIcon**](LiveActivityAlertIcon.md) | Optional SF Symbol icon. Supported by alert, progress, segmented_progress, metrics, stats, and timer. | [optional] 
**badge** | [**LiveActivityAlertBadge**](LiveActivityAlertBadge.md) | Optional badge. Supported by alert, progress, and segmented_progress. | [optional] 
**type** | **str** |  | 
**color** | **str** | Optional. Accent color for progress, segmented_progress, metrics, and timer Live Activities. For Alert Live Activities, this tints action and secondary_action buttons when included. | [optional] 
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to type&#x3D;segmented_progress. | [optional] 
**step_colors** | **List[str]** | Optional. Colors for completed steps. When used with segmented_progress, the array length should match current_step. | [optional] 

## Example

```python
from activitysmith_openapi.models.content_state_start import ContentStateStart

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStateStart from a JSON string
content_state_start_instance = ContentStateStart.from_json(json)
# print the JSON string representation of the object
print(ContentStateStart.to_json())

# convert the object into a dict
content_state_start_dict = content_state_start_instance.to_dict()
# create an instance of ContentStateStart from a dict
content_state_start_from_dict = ContentStateStart.from_dict(content_state_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


