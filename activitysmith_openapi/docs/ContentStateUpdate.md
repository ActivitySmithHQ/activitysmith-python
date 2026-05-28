# ContentStateUpdate

Update payload requires title. For segmented_progress include current_step and optionally number_of_steps. For progress include percentage or value with upper_limit. For metrics and stats include a non-empty metrics array. For alert include message, with optional icon and badge. Type is optional when updating an existing activity. You can increase or decrease number_of_steps during updates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Total number of steps. Use for type&#x3D;segmented_progress. Optional on update, and safe to change if the workflow gains or loses steps. | [optional] 
**current_step** | **int** | Current step. Use for type&#x3D;segmented_progress. | [optional] 
**percentage** | **float** | Progress percentage (0–100). Use for type&#x3D;progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for type&#x3D;progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for type&#x3D;progress. | [optional] 
**metrics** | [**List[ActivityMetric]**](ActivityMetric.md) | Use for type&#x3D;metrics or type&#x3D;stats. | [optional] 
**message** | **str** | Alert message. Use for type&#x3D;alert. | [optional] 
**icon** | [**LiveActivityAlertIcon**](LiveActivityAlertIcon.md) | Optional SF Symbol icon for type&#x3D;alert. | [optional] 
**badge** | [**LiveActivityAlertBadge**](LiveActivityAlertBadge.md) | Optional badge for type&#x3D;alert. | [optional] 
**type** | **str** | Optional. When omitted, the API uses the existing Live Activity type. | [optional] 
**color** | **str** | Optional. Accent color for progress, segmented_progress, and metrics Live Activities. For Alert Live Activities, this tints the action button when action is included. | [optional] 
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


