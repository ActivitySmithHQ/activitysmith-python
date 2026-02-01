# ContentStateStart

Start payload requires title, number_of_steps, current_step, and type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** |  | 
**current_step** | **int** |  | 
**type** | **str** |  | 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. | [optional] 

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


