# PushNotificationReplaceResponse

Apple APNs acceptance result for the replacement. Acceptance does not confirm device delivery or presentation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when APNs accepts the replacement for at least one device. | 
**notification_id** | **str** | ID of the replaced Push Notification. It stays the same, so you can replace it again. | 
**devices_notified** | **int** | Number of device tokens for which APNs accepted the notification, without confirming on-device delivery. | [optional] 
**users_notified** | **int** |  | [optional] 
**effective_channel_slugs** | **List[str]** |  | [optional] 
**tags** | **List[str]** | Optional tags to organize and filter notification history. | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.push_notification_replace_response import PushNotificationReplaceResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationReplaceResponse from a JSON string
push_notification_replace_response_instance = PushNotificationReplaceResponse.from_json(json)
# print the JSON string representation of the object
print(PushNotificationReplaceResponse.to_json())

# convert the object into a dict
push_notification_replace_response_dict = push_notification_replace_response_instance.to_dict()
# create an instance of PushNotificationReplaceResponse from a dict
push_notification_replace_response_from_dict = PushNotificationReplaceResponse.from_dict(push_notification_replace_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


