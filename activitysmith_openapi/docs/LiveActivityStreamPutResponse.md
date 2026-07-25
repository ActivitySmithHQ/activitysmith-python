# LiveActivityStreamPutResponse

Returned after a managed stream request is reconciled.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**operation** | **str** |  | 
**stream_key** | **str** |  | 
**activity_id** | **str** |  | [optional] 
**previous_activity_id** | **str** |  | [optional] 
**devices_notified** | **int** |  | [optional] 
**devices_queued** | **int** |  | [optional] 
**users_notified** | **int** |  | [optional] 
**effective_channel_slugs** | **List[str]** |  | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.live_activity_stream_put_response import LiveActivityStreamPutResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStreamPutResponse from a JSON string
live_activity_stream_put_response_instance = LiveActivityStreamPutResponse.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStreamPutResponse.to_json())

# convert the object into a dict
live_activity_stream_put_response_dict = live_activity_stream_put_response_instance.to_dict()
# create an instance of LiveActivityStreamPutResponse from a dict
live_activity_stream_put_response_from_dict = LiveActivityStreamPutResponse.from_dict(live_activity_stream_put_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


