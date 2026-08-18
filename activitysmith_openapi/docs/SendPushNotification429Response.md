# SendPushNotification429Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 
**limit** | **int** |  | 
**blocked_devices** | **int** | Number of targeted devices that have reached the enforced iOS Live Activity concurrency threshold. | 

## Example

```python
from activitysmith_openapi.models.send_push_notification429_response import SendPushNotification429Response

# TODO update the JSON string below
json = "{}"
# create an instance of SendPushNotification429Response from a JSON string
send_push_notification429_response_instance = SendPushNotification429Response.from_json(json)
# print the JSON string representation of the object
print(SendPushNotification429Response.to_json())

# convert the object into a dict
send_push_notification429_response_dict = send_push_notification429_response_instance.to_dict()
# create an instance of SendPushNotification429Response from a dict
send_push_notification429_response_from_dict = SendPushNotification429Response.from_dict(send_push_notification429_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


