# LiveActivityEndRequest

End an existing Live Activity by activity_id.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Additional information shown in notification and Live Activity details in ActivitySmith. Not displayed in the Push Notification or Live Activity on the device. Values must be strings, finite numbers, or booleans. At most 50 entries and 16 KB of serialized UTF-8 JSON. Omit on updates to preserve existing Metadata; send {} to clear it. | [optional] 
**activity_id** | **str** |  | 
**tags** | **List[str]** | Tags for notification history. Omit to keep existing Tags, supply an array to replace them, or send an empty array to clear them. | [optional] 
**content_state** | [**ContentStateEnd**](ContentStateEnd.md) |  | 
**action** | [**LiveActivityAction**](LiveActivityAction.md) |  | [optional] 
**secondary_action** | [**LiveActivityAction**](LiveActivityAction.md) | Optional secondary action button. Supported for alert, progress, and segmented_progress Live Activities. Uses the same open_url, shortcuts://, and webhook shapes as action. | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_end_request import LiveActivityEndRequest

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


