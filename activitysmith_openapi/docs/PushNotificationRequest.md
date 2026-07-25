# PushNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**message** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 
**media** | **str** | Optional HTTPS URL for an image, audio file, or video that users can preview or play when they expand the notification. If &#x60;redirection&#x60; is omitted, tapping the notification opens this URL. Cannot be combined with &#x60;actions&#x60;. | [optional] 
**redirection** | **str** | Optional HTTP URL, HTTPS URL, or shortcuts://run-shortcut?name&#x3D;... URL opened when the user taps the notification body. Use shortcuts://run-shortcut?name&#x3D;... to run a specific iPhone Shortcut that already exists on the user&#39;s device. Overrides the default tap target from &#x60;media&#x60; when both are provided. | [optional] 
**actions** | [**List[PushNotificationAction]**](PushNotificationAction.md) | Optional interactive actions shown when users expand the notification. Cannot be combined with &#x60;media&#x60;. | [optional] 
**payload** | **object** |  | [optional] 
**badge** | **int** |  | [optional] 
**sound** | **str** |  | [optional] 
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


