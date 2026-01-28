# LiveActivityEndRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**activity_id** | **str** |  | 
**content_state** | [**ContentStateEnd**](ContentStateEnd.md) |  | 

## Example

```python
from openapi_client.models.live_activity_end_request import LiveActivityEndRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityEndRequest from a JSON string
live_activity_end_request_instance = LiveActivityEndRequest.from_json(json)
# print the JSON string representation of the object
print(LiveActivityEndRequest.to_json())

# convert the object into a dict
live_activity_end_request_dict = live_activity_end_request_instance.to_dict()
# create an instance of LiveActivityEndRequest from a dict
live_activity_end_request_from_dict = LiveActivityEndRequest.from_dict(live_activity_end_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


