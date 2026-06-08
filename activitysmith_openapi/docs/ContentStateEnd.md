# ContentStateEnd

End payload requires title. For segmented_progress include current_step and optionally number_of_steps. For progress include percentage or value with upper_limit. For metrics and stats include a non-empty metrics array. For alert include message. For timer, omit duration_seconds to preserve and freeze the latest timer state. Optional icon is supported by all Live Activity types. Optional badge is supported by alert, progress, and segmented_progress. Type is optional when ending an existing activity. You can send an updated number_of_steps here if the workflow changed after start.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Total number of steps. Use for type&#x3D;segmented_progress. Optional on end, and safe to change if the final workflow used more or fewer steps than originally planned. | [optional] 
**current_step** | **int** | Current completed step count. Use for type&#x3D;segmented_progress. Must be less than or equal to number_of_steps when number_of_steps is provided. | [optional] 
**percentage** | **float** | Progress percentage (0–100). Use for type&#x3D;progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for type&#x3D;progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for type&#x3D;progress. | [optional] 
**duration_seconds** | **float** | Timer duration in seconds. For type&#x3D;timer, omit duration_seconds on end to preserve and freeze the latest timer state. | [optional] 
**counts_down** | **bool** | Use with type&#x3D;timer. When true or omitted, the timer counts down from duration_seconds. Set false for an elapsed timer; omit duration_seconds for an open-ended elapsed timer. | [optional] [default to True]
**is_running** | **bool** | Use with type&#x3D;timer. Defaults to true. Set false to pause/freeze via API; set true on a paused timer to resume. | [optional] [default to True]
**metrics** | [**List[ActivityMetric]**](ActivityMetric.md) | Use for type&#x3D;metrics or type&#x3D;stats. | [optional] 
**message** | **str** | Alert message. Use for type&#x3D;alert. | [optional] 
**icon** | [**LiveActivityAlertIcon**](LiveActivityAlertIcon.md) | Optional SF Symbol icon. Supported by alert, progress, segmented_progress, metrics, stats, and timer. | [optional] 
**badge** | [**LiveActivityAlertBadge**](LiveActivityAlertBadge.md) | Optional badge. Supported by alert, progress, and segmented_progress. | [optional] 
**type** | **str** | Optional. When omitted, the API uses the existing Live Activity type. | [optional] 
**color** | **str** | Optional. Accent color for progress, segmented_progress, metrics, and timer Live Activities. For Alert Live Activities, this tints the action button when action is included. | [optional] 
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to type&#x3D;segmented_progress. | [optional] 
**step_colors** | **List[str]** | Optional. Colors for completed steps. When used with segmented_progress, the array length should match current_step. | [optional] 
**auto_dismiss_minutes** | **int** | Optional. Minutes before the ended Live Activity is dismissed. Default 3. Set 0 for immediate dismissal. iOS will dismiss ended Live Activities after ~4 hours max. | [optional] [default to 3]

## Example

```python
from activitysmith_openapi.models.content_state_end import ContentStateEnd

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStateEnd from a JSON string
content_state_end_instance = ContentStateEnd.from_json(json)
# print the JSON string representation of the object
print(ContentStateEnd.to_json())

# convert the object into a dict
content_state_end_dict = content_state_end_instance.to_dict()
# create an instance of ContentStateEnd from a dict
content_state_end_from_dict = ContentStateEnd.from_dict(content_state_end_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


