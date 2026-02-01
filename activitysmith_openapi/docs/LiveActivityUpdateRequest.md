# LiveActivityUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** |  | 
**content_state** | [**ContentStateUpdate**](ContentStateUpdate.md) |  | 

## Example

```python
from activitysmith_openapi.models.live_activity_update_request import LiveActivityUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityUpdateRequest from a JSON string
live_activity_update_request_instance = LiveActivityUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(LiveActivityUpdateRequest.to_json())

# convert the object into a dict
live_activity_update_request_dict = live_activity_update_request_instance.to_dict()
# create an instance of LiveActivityUpdateRequest from a dict
live_activity_update_request_from_dict = LiveActivityUpdateRequest.from_dict(live_activity_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


