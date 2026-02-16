# LiveActivityStartResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**devices_notified** | **int** |  | [optional] 
**users_notified** | **int** |  | [optional] 
**activity_id** | **str** |  | 
**effective_channel_slugs** | **List[str]** |  | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.live_activity_start_response import LiveActivityStartResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStartResponse from a JSON string
live_activity_start_response_instance = LiveActivityStartResponse.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStartResponse.to_json())

# convert the object into a dict
live_activity_start_response_dict = live_activity_start_response_instance.to_dict()
# create an instance of LiveActivityStartResponse from a dict
live_activity_start_response_from_dict = LiveActivityStartResponse.from_dict(live_activity_start_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


