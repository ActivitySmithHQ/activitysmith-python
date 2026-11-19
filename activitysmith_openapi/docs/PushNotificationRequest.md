# PushNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Additional information shown in notification and Live Activity details in ActivitySmith. Not displayed in the Push Notification or Live Activity on the device. Values must be strings, finite numbers, or booleans. At most 50 entries and 16 KB of serialized UTF-8 JSON. Omit on updates to preserve existing Metadata; send {} to clear it. | [optional] 
**title** | **str** |  | 
**message** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**icon** | **str** | Optional HTTPS image URL without credentials for a custom notification icon. If the image cannot be loaded, the app icon is used. iOS may omit subtitle when displaying a custom icon. | [optional] 
**interruption_level** | [**PushInterruptionLevel**](PushInterruptionLevel.md) | Optional. How urgently iOS presents the notification: &#x60;passive&#x60; (quiet, no sound or screen wake), &#x60;active&#x60; (default), or &#x60;time-sensitive&#x60; (can break through Focus and Scheduled Summary when allowed). Omit for normal delivery. | [optional] 
**media** | **str** | Optional HTTPS URL for an image, audio file, or video that users can preview or play when they expand the notification. If &#x60;redirection&#x60; is omitted, tapping the notification opens this URL. Cannot be combined with &#x60;actions&#x60;. | [optional] 
**redirection** | **str** | Optional HTTP, HTTPS, Shortcuts, or installed app URL opened when the user taps the notification body. Custom schemes such as spotify:// and spotify:track:123 require iOS 1.13.4 build 2 or later and an installed handler; no web fallback is provided. Internal and executable schemes are blocked. Overrides the default tap target from media. | [optional] 
**actions** | [**List[PushNotificationAction]**](PushNotificationAction.md) | Optional interactive actions shown when users expand the notification. Cannot be combined with &#x60;media&#x60;. | [optional] 
**payload** | **object** |  | [optional] 
**badge** | **int** |  | [optional] 
**sound** | **str** | Optional sound for this Push Notification. Omit it to play the Push Notifications sound picked on the device. Passive Push Notifications play no sound. Sounds bundled with the ActivitySmith app: &#x60;arrive&#x60;, &#x60;bell&#x60;, &#x60;bells&#x60;, &#x60;bitflip&#x60;, &#x60;bloom&#x60;, &#x60;callout&#x60;, &#x60;chime&#x60;, &#x60;coin&#x60;, &#x60;corrupt&#x60;, &#x60;crest&#x60;, &#x60;cue&#x60;, &#x60;ding&#x60;, &#x60;drop&#x60;, &#x60;ember&#x60;, &#x60;emblem&#x60;, &#x60;flourish&#x60;, &#x60;glimmer&#x60;, &#x60;glint&#x60;, &#x60;glitch&#x60;, &#x60;lantern&#x60;, &#x60;nightfall&#x60;, &#x60;nudge&#x60;, &#x60;pixel&#x60;, &#x60;pop&#x60;, &#x60;signal&#x60;, &#x60;streak&#x60;, &#x60;tally&#x60;, &#x60;wand&#x60;, &#x60;whoosh&#x60;, &#x60;zip&#x60;. Use &#x60;default&#x60; for the sound picked on the device, or &#x60;none&#x60; for no sound. | [optional] 
**target** | [**ChannelTarget**](ChannelTarget.md) |  | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 

## Example

```python
from activitysmith_openapi.models.push_notification_request import PushNotificationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationRequest from a JSON string
push_notification_request_instance = PushNotificationRequest.from_json(json)
# print the JSON string representation of the object
print(PushNotificationRequest.to_json())

# convert the object into a dict
push_notification_request_dict = push_notification_request_instance.to_dict()
# create an instance of PushNotificationRequest from a dict
push_notification_request_from_dict = PushNotificationRequest.from_dict(push_notification_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


