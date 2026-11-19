# LiveActivityStreamDeleteRequest

Optional payload for ending a managed stream. When omitted, ActivitySmith ends the stream using the latest known state when possible.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Additional information shown in notification and Live Activity details in ActivitySmith. Not displayed in the Push Notification or Live Activity on the device. Values must be strings, finite numbers, or booleans. At most 50 entries and 16 KB of serialized UTF-8 JSON. Omit on updates to preserve existing Metadata; send {} to clear it. | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 
**content_state** | [**StreamContentState**](StreamContentState.md) |  | [optional] 
**action** | [**LiveActivityAction**](LiveActivityAction.md) |  | [optional] 
**secondary_action** | [**LiveActivityAction**](LiveActivityAction.md) | Optional secondary action button. Supported for alert, progress, segmented_progress, and value Live Activities. Uses the same open_url, shortcuts://, and webhook shapes as action. | [optional] 
**alert** | [**AlertPayload**](AlertPayload.md) |  | [optional] 
**sound** | **str** | Optional sound for the end. Ends are silent unless you set one. A sound also expands the Live Activity on the Lock Screen. Sounds bundled with the ActivitySmith app: &#x60;arrive&#x60;, &#x60;bell&#x60;, &#x60;bells&#x60;, &#x60;bitflip&#x60;, &#x60;bloom&#x60;, &#x60;callout&#x60;, &#x60;chime&#x60;, &#x60;coin&#x60;, &#x60;corrupt&#x60;, &#x60;crest&#x60;, &#x60;cue&#x60;, &#x60;ding&#x60;, &#x60;drop&#x60;, &#x60;ember&#x60;, &#x60;emblem&#x60;, &#x60;flourish&#x60;, &#x60;glimmer&#x60;, &#x60;glint&#x60;, &#x60;glitch&#x60;, &#x60;lantern&#x60;, &#x60;nightfall&#x60;, &#x60;nudge&#x60;, &#x60;pixel&#x60;, &#x60;pop&#x60;, &#x60;signal&#x60;, &#x60;streak&#x60;, &#x60;tally&#x60;, &#x60;wand&#x60;, &#x60;whoosh&#x60;, &#x60;zip&#x60;. Use &#x60;default&#x60; for the sound picked on the device, or &#x60;none&#x60; for no sound. Bundled sounds and &#x60;none&#x60; need iOS app 1.19.0 or later. Older apps play the iOS default sound instead. | [optional] 

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


