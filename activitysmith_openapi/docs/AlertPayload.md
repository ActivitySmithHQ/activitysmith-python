# AlertPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**body** | **str** |  | [optional] 

## Example

```python
from activitysmith_openapi.models.alert_payload import AlertPayload

# TODO update the JSON string below
json = "{}"
# create an instance of AlertPayload from a JSON string
alert_payload_instance = AlertPayload.from_json(json)
# print the JSON string representation of the object
print(AlertPayload.to_json())

# convert the object into a dict
alert_payload_dict = alert_payload_instance.to_dict()
# create an instance of AlertPayload from a dict
alert_payload_from_dict = AlertPayload.from_dict(alert_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


