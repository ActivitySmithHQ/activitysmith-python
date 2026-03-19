# LiveActivityAction

Optional single action button shown in the Live Activity UI.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Button title displayed in the Live Activity UI. | 
**type** | [**LiveActivityActionType**](LiveActivityActionType.md) |  | 
**url** | **str** | HTTPS URL. For open_url it is opened in browser. For webhook it is called by ActivitySmith backend. | 
**method** | [**LiveActivityWebhookMethod**](LiveActivityWebhookMethod.md) | Webhook HTTP method. Used only when type&#x3D;webhook. | [optional] [default to LiveActivityWebhookMethod.POST]
**body** | **Dict[str, object]** | Optional webhook payload body. Used only when type&#x3D;webhook. | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_action import LiveActivityAction

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityAction from a JSON string
live_activity_action_instance = LiveActivityAction.from_json(json)
# print the JSON string representation of the object
print(LiveActivityAction.to_json())

# convert the object into a dict
live_activity_action_dict = live_activity_action_instance.to_dict()
# create an instance of LiveActivityAction from a dict
live_activity_action_from_dict = LiveActivityAction.from_dict(live_activity_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


