# PushNotificationDismissResponse

Dismissal result. Devices clear the notification after this response, so it does not confirm that any device has cleared it.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | True when the dismissal is recorded. | 
**notification_id** | **str** | ID of the dismissed Push Notification. | 
**dismissed_at** | **datetime** | When the notification was first dismissed. Repeat calls return the same time. | 

## Example

```python
from activitysmith_openapi.models.push_notification_dismiss_response import PushNotificationDismissResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationDismissResponse from a JSON string
push_notification_dismiss_response_instance = PushNotificationDismissResponse.from_json(json)
# print the JSON string representation of the object
print(PushNotificationDismissResponse.to_json())

# convert the object into a dict
push_notification_dismiss_response_dict = push_notification_dismiss_response_instance.to_dict()
# create an instance of PushNotificationDismissResponse from a dict
push_notification_dismiss_response_from_dict = PushNotificationDismissResponse.from_dict(push_notification_dismiss_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


