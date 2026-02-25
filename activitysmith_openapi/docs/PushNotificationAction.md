# PushNotificationAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Button title displayed in iOS expanded notification UI. | 
**type** | [**PushNotificationActionType**](PushNotificationActionType.md) |  | 
**url** | **str** | HTTPS URL. For open_url it is opened in browser. For webhook it is called by ActivitySmith backend. | 
**method** | [**PushNotificationWebhookMethod**](PushNotificationWebhookMethod.md) | Webhook HTTP method. Used only when type&#x3D;webhook. | [optional] [default to PushNotificationWebhookMethod.POST]
**body** | **Dict[str, object]** | Optional webhook payload body. Used only when type&#x3D;webhook. | [optional] 

## Example

```python
from activitysmith_openapi.models.push_notification_action import PushNotificationAction

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationAction from a JSON string
push_notification_action_instance = PushNotificationAction.from_json(json)
# print the JSON string representation of the object
print(PushNotificationAction.to_json())

# convert the object into a dict
push_notification_action_dict = push_notification_action_instance.to_dict()
# create an instance of PushNotificationAction from a dict
push_notification_action_from_dict = PushNotificationAction.from_dict(push_notification_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


