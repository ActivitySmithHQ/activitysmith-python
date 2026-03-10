# ContentStateStart

Start payload requires title and type. For segmented_progress include number_of_steps and current_step. For progress include percentage or value with upper_limit.

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
**type** | **str** |  | 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to type&#x3D;segmented_progress. | [optional] 

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


