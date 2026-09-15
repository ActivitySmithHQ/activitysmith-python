# LiveActivityLimitError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 
**limit** | **int** |  | 
**active** | **int** | Highest number of active Live Activities among the targeted devices. | 
**blocked_devices** | **int** | Number of targeted devices that have reached the enforced iOS Live Activity concurrency threshold. Included only when targeted devices have mixed capacity. | [optional] 
**targeted_devices** | **int** | Total number of targeted devices. Included only when targeted devices have mixed capacity. | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_limit_error import LiveActivityLimitError

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityLimitError from a JSON string
live_activity_limit_error_instance = LiveActivityLimitError.from_json(json)
# print the JSON string representation of the object
print(LiveActivityLimitError.to_json())

# convert the object into a dict
live_activity_limit_error_dict = live_activity_limit_error_instance.to_dict()
# create an instance of LiveActivityLimitError from a dict
live_activity_limit_error_from_dict = LiveActivityLimitError.from_dict(live_activity_limit_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


