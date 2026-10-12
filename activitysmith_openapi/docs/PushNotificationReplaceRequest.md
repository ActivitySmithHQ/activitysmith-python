# PushNotificationReplaceRequest

Replacement content. title, subtitle, message, redirection, media, icon, actions, and payload fully replace the original values. Omit metadata or tags to keep the stored values; send {} or [] to clear them.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Dict[str, MetadataValue]**](MetadataValue.md) | Additional information shown in notification and Live Activity details in ActivitySmith. Not displayed in the Push Notification or Live Activity on the device. Values must be strings, finite numbers, or booleans. At most 50 entries and 16 KB of serialized UTF-8 JSON. Omit on updates to preserve existing Metadata; send {} to clear it. | [optional] 
**title** | **str** |  | 
**message** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**icon** | **str** | Optional HTTPS image URL without credentials for a custom notification icon. If the image cannot be loaded, the app icon is used. iOS may omit subtitle when displaying a custom icon. | [optional] 
**media** | **str** | Optional HTTPS URL for an image, audio file, or video that users can preview or play when they expand the notification. If &#x60;redirection&#x60; is omitted, tapping the notification opens this URL. Cannot be combined with &#x60;actions&#x60;. | [optional] 
**redirection** | **str** | Optional HTTP, HTTPS, Shortcuts, or installed app URL opened when the user taps the notification body. Custom schemes such as spotify:// and spotify:track:123 require iOS 1.13.4 build 2 or later and an installed handler; no web fallback is provided. Internal and executable schemes are blocked. Overrides the default tap target from media. | [optional] 
**actions** | [**List[PushNotificationAction]**](PushNotificationAction.md) | Optional interactive actions shown when users expand the notification. Cannot be combined with &#x60;media&#x60;. | [optional] 
**payload** | **object** |  | [optional] 
**badge** | **int** |  | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 

## Example

```python
from activitysmith_openapi.models.push_notification_replace_request import PushNotificationReplaceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationReplaceRequest from a JSON string
push_notification_replace_request_instance = PushNotificationReplaceRequest.from_json(json)
# print the JSON string representation of the object
print(PushNotificationReplaceRequest.to_json())

# convert the object into a dict
push_notification_replace_request_dict = push_notification_replace_request_instance.to_dict()
# create an instance of PushNotificationReplaceRequest from a dict
push_notification_replace_request_from_dict = PushNotificationReplaceRequest.from_dict(push_notification_replace_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


