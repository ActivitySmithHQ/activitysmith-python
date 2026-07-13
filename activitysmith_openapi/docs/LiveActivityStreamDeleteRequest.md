# LiveActivityStreamDeleteRequest

Optional payload for ending a managed stream. When omitted, ActivitySmith ends the stream using the latest known state when possible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_state** | [**StreamContentState**](StreamContentState.md) |  | [optional] 
**action** | [**LiveActivityAction**](LiveActivityAction.md) |  | [optional] 
**secondary_action** | [**LiveActivityAction**](LiveActivityAction.md) | Optional secondary action button. Supported for alert, progress, and segmented_progress Live Activities. Uses the same open_url, shortcuts://, and webhook shapes as action. | [optional] 
**alert** | [**AlertPayload**](AlertPayload.md) |  | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_stream_delete_request import LiveActivityStreamDeleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStreamDeleteRequest from a JSON string
live_activity_stream_delete_request_instance = LiveActivityStreamDeleteRequest.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStreamDeleteRequest.to_json())

# convert the object into a dict
live_activity_stream_delete_request_dict = live_activity_stream_delete_request_instance.to_dict()
# create an instance of LiveActivityStreamDeleteRequest from a dict
live_activity_stream_delete_request_from_dict = LiveActivityStreamDeleteRequest.from_dict(live_activity_stream_delete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


