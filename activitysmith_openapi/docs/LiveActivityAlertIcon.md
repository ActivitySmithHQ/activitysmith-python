# LiveActivityAlertIcon

Optional SF Symbol icon for Alert Live Activities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**symbol** | **str** | Apple SF Symbol name. | 
**color** | [**LiveActivityColor**](LiveActivityColor.md) | Optional icon color. | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_alert_icon import LiveActivityAlertIcon

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityAlertIcon from a JSON string
live_activity_alert_icon_instance = LiveActivityAlertIcon.from_json(json)
# print the JSON string representation of the object
print(LiveActivityAlertIcon.to_json())

# convert the object into a dict
live_activity_alert_icon_dict = live_activity_alert_icon_instance.to_dict()
# create an instance of LiveActivityAlertIcon from a dict
live_activity_alert_icon_from_dict = LiveActivityAlertIcon.from_dict(live_activity_alert_icon_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


