# LiveActivityValue

A formatted string or finite numeric Live Activity value. String formatting is preserved.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------

## Example

```python
from activitysmith_openapi.models.live_activity_value import LiveActivityValue

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityValue from a JSON string
live_activity_value_instance = LiveActivityValue.from_json(json)
# print the JSON string representation of the object
print(LiveActivityValue.to_json())

# convert the object into a dict
live_activity_value_dict = live_activity_value_instance.to_dict()
# create an instance of LiveActivityValue from a dict
live_activity_value_from_dict = LiveActivityValue.from_dict(live_activity_value_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


