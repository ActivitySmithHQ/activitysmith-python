# ContentStateUpdate

Update payload requires title. For segmented_progress include current_step and optionally number_of_steps. For progress include percentage or value with upper_limit. For metrics and stats include a non-empty metrics array. For alert include message. For timer, omit duration_seconds to preserve the current timer window or send duration_seconds to reset the timer from the update request time. Optional icon is supported by all Live Activity types. Optional badge is supported by alert, progress, and segmented_progress. Type is optional when updating an existing activity. You can increase or decrease number_of_steps during updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Total number of steps. Use for type&#x3D;segmented_progress. Optional on update, and safe to change if the workflow gains or loses steps. | [optional] 
**current_step** | **int** | Current completed step count. Use for type&#x3D;segmented_progress. Set 0 when no segment is complete yet. Must be less than or equal to number_of_steps when number_of_steps is provided. | [optional] 
**percentage** | **float** | Progress percentage (0–100). Use for type&#x3D;progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for type&#x3D;progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for type&#x3D;progress. | [optional] 
**duration_seconds** | **float** | Timer duration in seconds. For type&#x3D;timer, sending duration_seconds resets the timer window from the update request time; omit it to preserve the existing timer window. | [optional] 
**counts_down** | **bool** | Use with type&#x3D;timer. When true or omitted, the timer counts down from duration_seconds. Set false for an elapsed timer; omit duration_seconds for an open-ended elapsed timer. | [optional] [default to True]
**is_running** | **bool** | Use with type&#x3D;timer. Defaults to true. Set false to pause/freeze via API; set true on a paused timer to resume. | [optional] [default to True]
**metrics** | [**List[ActivityMetric]**](ActivityMetric.md) | Use for type&#x3D;metrics or type&#x3D;stats. | [optional] 
**message** | **str** | Alert message. Use for type&#x3D;alert. | [optional] 
**icon** | [**LiveActivityAlertIcon**](LiveActivityAlertIcon.md) | Optional SF Symbol icon. Supported by alert, progress, segmented_progress, metrics, stats, and timer. | [optional] 
**badge** | [**LiveActivityAlertBadge**](LiveActivityAlertBadge.md) | Optional badge. Supported by alert, progress, and segmented_progress. | [optional] 
**type** | **str** | Optional. When omitted, the API uses the existing Live Activity type. | [optional] 
**color** | **str** | Optional. Accent color for progress, segmented_progress, metrics, and timer Live Activities. For Alert Live Activities, this tints action and secondary_action buttons when included. | [optional] 
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to type&#x3D;segmented_progress. | [optional] 
**step_colors** | **List[str]** | Optional. Colors for completed steps. When used with segmented_progress, the array length should match current_step. | [optional] 

## Example

```python
from activitysmith_openapi.models.content_state_update import ContentStateUpdate

# TODO update the JSON string below
json = "{}"
# create an instance of ContentStateUpdate from a JSON string
content_state_update_instance = ContentStateUpdate.from_json(json)
# print the JSON string representation of the object
print(ContentStateUpdate.to_json())

# convert the object into a dict
content_state_update_dict = content_state_update_instance.to_dict()
# create an instance of ContentStateUpdate from a dict
content_state_update_from_dict = ContentStateUpdate.from_dict(content_state_update_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


