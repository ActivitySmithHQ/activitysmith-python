# PushNotificationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**devices_notified** | **int** |  | [optional] 
**users_notified** | **int** |  | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.push_notification_response import PushNotificationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PushNotificationResponse from a JSON string
push_notification_response_instance = PushNotificationResponse.from_json(json)
# print the JSON string representation of the object
print(PushNotificationResponse.to_json())

# convert the object into a dict
push_notification_response_dict = push_notification_response_instance.to_dict()
# create an instance of PushNotificationResponse from a dict
push_notification_response_from_dict = PushNotificationResponse.from_dict(push_notification_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


