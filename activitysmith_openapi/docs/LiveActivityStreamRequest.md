# LiveActivityStreamRequest

Send the latest state for a managed Live Activity stream. channels is the streamlined form for stream targeting. target.channels is also accepted for compatibility. If both are provided, they must match.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Additional information shown in notification and Live Activity details in ActivitySmith. Not displayed in the Push Notification or Live Activity on the device. Values must be strings, finite numbers, or booleans. At most 50 entries and 16 KB of serialized UTF-8 JSON. Omit on updates to preserve existing Metadata; send {} to clear it. | [optional] 
**content_state** | [**StreamContentState**](StreamContentState.md) |  | 
**action** | [**LiveActivityAction**](LiveActivityAction.md) |  | [optional] 
**secondary_action** | [**LiveActivityAction**](LiveActivityAction.md) | Optional secondary action button. Supported for alert, progress, segmented_progress, and value Live Activities. Uses the same open_url, shortcuts://, and webhook shapes as action. | [optional] 
**alert** | [**AlertPayload**](AlertPayload.md) |  | [optional] 
**channels** | **List[str]** | Channel slugs. When omitted, API key scope determines recipients. | [optional] 
**target** | [**ChannelTarget**](ChannelTarget.md) |  | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 
**sound** | **str** | Optional sound for this call. A call that starts a Live Activity plays the Live Activities sound picked on the device unless you set one. Updates are silent unless you set one. iOS plays an update sound only while the screen is on. Sounds bundled with the ActivitySmith app: &#x60;arrive&#x60;, &#x60;bell&#x60;, &#x60;bells&#x60;, &#x60;bitflip&#x60;, &#x60;bloom&#x60;, &#x60;callout&#x60;, &#x60;chime&#x60;, &#x60;coin&#x60;, &#x60;corrupt&#x60;, &#x60;crest&#x60;, &#x60;cue&#x60;, &#x60;ding&#x60;, &#x60;drop&#x60;, &#x60;ember&#x60;, &#x60;emblem&#x60;, &#x60;flourish&#x60;, &#x60;glimmer&#x60;, &#x60;glint&#x60;, &#x60;glitch&#x60;, &#x60;lantern&#x60;, &#x60;nightfall&#x60;, &#x60;nudge&#x60;, &#x60;pixel&#x60;, &#x60;pop&#x60;, &#x60;signal&#x60;, &#x60;streak&#x60;, &#x60;tally&#x60;, &#x60;wand&#x60;, &#x60;whoosh&#x60;, &#x60;zip&#x60;. Use &#x60;default&#x60; for the sound picked on the device, or &#x60;none&#x60; for no sound. | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_stream_request import LiveActivityStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStreamRequest from a JSON string
live_activity_stream_request_instance = LiveActivityStreamRequest.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStreamRequest.to_json())

# convert the object into a dict
live_activity_stream_request_dict = live_activity_stream_request_instance.to_dict()
# create an instance of LiveActivityStreamRequest from a dict
live_activity_stream_request_from_dict = LiveActivityStreamRequest.from_dict(live_activity_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


