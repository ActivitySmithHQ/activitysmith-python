# ContentStateUpdate

Update payload. Required fields are title and current_step. number_of_steps is optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** |  | [optional] 
**current_step** | **int** |  | 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. | [optional] 

## Example

```python
from openapi_client.models.content_state_update import ContentStateUpdate

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


