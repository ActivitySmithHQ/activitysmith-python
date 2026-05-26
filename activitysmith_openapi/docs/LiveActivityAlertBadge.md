# LiveActivityAlertBadge

Optional badge for alert Live Activities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**color** | [**LiveActivityColor**](LiveActivityColor.md) | Optional badge color. | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_alert_badge import LiveActivityAlertBadge

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityAlertBadge from a JSON string
live_activity_alert_badge_instance = LiveActivityAlertBadge.from_json(json)
# print the JSON string representation of the object
print(LiveActivityAlertBadge.to_json())

# convert the object into a dict
live_activity_alert_badge_dict = live_activity_alert_badge_instance.to_dict()
# create an instance of LiveActivityAlertBadge from a dict
live_activity_alert_badge_from_dict = LiveActivityAlertBadge.from_dict(live_activity_alert_badge_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


