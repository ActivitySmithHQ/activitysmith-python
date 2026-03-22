# LiveActivityStreamDeleteResponse

Returned after a managed stream is ended and removed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**operation** | **str** |  | 
**stream_key** | **str** |  | 
**activity_id** | **str** |  | [optional] 
**devices_queued** | **int** |  | [optional] 
**devices_notified** | **int** |  | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.live_activity_stream_delete_response import LiveActivityStreamDeleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStreamDeleteResponse from a JSON string
live_activity_stream_delete_response_instance = LiveActivityStreamDeleteResponse.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStreamDeleteResponse.to_json())

# convert the object into a dict
live_activity_stream_delete_response_dict = live_activity_stream_delete_response_instance.to_dict()
# create an instance of LiveActivityStreamDeleteResponse from a dict
live_activity_stream_delete_response_from_dict = LiveActivityStreamDeleteResponse.from_dict(live_activity_stream_delete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


