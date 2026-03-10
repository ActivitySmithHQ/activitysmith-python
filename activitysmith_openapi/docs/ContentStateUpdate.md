# ContentStateUpdate

Update payload requires title. For segmented_progress include current_step and optionally number_of_steps. For progress include percentage or value with upper_limit. Type is optional when updating an existing activity.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Total number of steps. Use for type&#x3D;segmented_progress. | [optional] 
**current_step** | **int** | Current step. Use for type&#x3D;segmented_progress. | [optional] 
**percentage** | **float** | Progress percentage (0–100). Use for type&#x3D;progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for type&#x3D;progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for type&#x3D;progress. | [optional] 
**type** | **str** | Optional. When omitted, the API uses the existing Live Activity type. | [optional] 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to type&#x3D;segmented_progress. | [optional] 

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


