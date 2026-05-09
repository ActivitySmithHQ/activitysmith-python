# MetricValueUpdateRequest

Latest metric value to display in widgets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | [**MetricValueUpdateRequestValue**](MetricValueUpdateRequestValue.md) |  | 

## Example

```python
from activitysmith_openapi.models.metric_value_update_request import MetricValueUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetricValueUpdateRequest from a JSON string
metric_value_update_request_instance = MetricValueUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(MetricValueUpdateRequest.to_json())

# convert the object into a dict
metric_value_update_request_dict = metric_value_update_request_instance.to_dict()
# create an instance of MetricValueUpdateRequest from a dict
metric_value_update_request_from_dict = MetricValueUpdateRequest.from_dict(metric_value_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


