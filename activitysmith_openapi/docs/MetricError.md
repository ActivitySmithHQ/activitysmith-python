# MetricError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | [optional] 

## Example

```python
from activitysmith_openapi.models.metric_error import MetricError

# TODO update the JSON string below
json = "{}"
# create an instance of MetricError from a JSON string
metric_error_instance = MetricError.from_json(json)
# print the JSON string representation of the object
print(MetricError.to_json())

# convert the object into a dict
metric_error_dict = metric_error_instance.to_dict()
# create an instance of MetricError from a dict
metric_error_from_dict = MetricError.from_dict(metric_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


