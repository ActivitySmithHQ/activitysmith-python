# LiveActivityStreamDeleteRequest

Optional payload for ending a managed stream. When omitted, ActivitySmith ends the stream using the latest known state when possible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Additional information shown in notification and Live Activity details in ActivitySmith. Not displayed in the Push Notification or Live Activity on the device. Values must be strings, finite numbers, or booleans. At most 50 entries and 16 KB of serialized UTF-8 JSON. Omit on updates to preserve existing Metadata; send {} to clear it. | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 
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


