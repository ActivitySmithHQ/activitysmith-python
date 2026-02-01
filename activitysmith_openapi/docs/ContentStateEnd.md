# ContentStateEnd

End payload. Required fields are title and current_step. number_of_steps is optional.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** |  | [optional] 
**current_step** | **int** |  | 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. | [optional] 
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


