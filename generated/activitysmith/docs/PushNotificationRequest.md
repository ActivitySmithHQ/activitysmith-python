# PushNotificationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**message** | **str** |  | [optional] 
**subtitle** | **str** |  | [optional] 

## Example

```python
from activitysmith.models.push_notification_request import PushNotificationRequest

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


