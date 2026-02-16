# LiveActivityStartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_state** | [**ContentStateStart**](ContentStateStart.md) |  | 
**alert** | [**AlertPayload**](AlertPayload.md) |  | [optional] 
**target** | [**ChannelTarget**](ChannelTarget.md) |  | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_start_request import LiveActivityStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStartRequest from a JSON string
live_activity_start_request_instance = LiveActivityStartRequest.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStartRequest.to_json())

# convert the object into a dict
live_activity_start_request_dict = live_activity_start_request_instance.to_dict()
# create an instance of LiveActivityStartRequest from a dict
live_activity_start_request_from_dict = LiveActivityStartRequest.from_dict(live_activity_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


