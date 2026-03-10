# ContentStateEnd

End payload requires title. For segmented_progress include current_step and optionally number_of_steps. For progress include percentage or value with upper_limit. Type is optional when ending an existing activity. You can send an updated number_of_steps here if the workflow changed after start.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**subtitle** | **str** |  | [optional] 
**number_of_steps** | **int** | Total number of steps. Use for type&#x3D;segmented_progress. Optional on end, and safe to change if the final workflow used more or fewer steps than originally planned. | [optional] 
**current_step** | **int** | Current step. Use for type&#x3D;segmented_progress. | [optional] 
**percentage** | **float** | Progress percentage (0–100). Use for type&#x3D;progress. Takes precedence over value/upper_limit if both are provided. | [optional] 
**value** | **float** | Current progress value. Use with upper_limit for type&#x3D;progress. | [optional] 
**upper_limit** | **float** | Maximum progress value. Use with value for type&#x3D;progress. | [optional] 
**type** | **str** | Optional. When omitted, the API uses the existing Live Activity type. | [optional] 
**color** | **str** | Optional. Accent color for the Live Activity. Defaults to blue. | [optional] [default to 'blue']
**step_color** | **str** | Optional. Overrides color for the current step. Only applies to type&#x3D;segmented_progress. | [optional] 
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


