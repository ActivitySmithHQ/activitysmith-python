# MetricUpsertRequest

Metric definition. Omitted fields keep their current values, or use defaults for a new metric: a label made from the key and the number format.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | Name shown on the widget. | [optional] 
**format** | **str** | How widgets display the value: number (1,234), currency (requires currency_code), percent (send 99.9 to show 99.9%), unit (a number with a unit suffix, such as 120 ms), or string (text up to 64 characters). Defaults to number for a new metric. | [optional] 
**currency_code** | **str** | 3-letter ISO 4217 currency code, such as USD. Required for the currency format. | [optional] 
**unit** | **str** | Unit suffix for the unit format, such as ms or GB. | [optional] 
**unit_spacing** | **str** | For the unit format: none shows 120ms, space shows 120 ms. | [optional] 

## Example

```python
from activitysmith_openapi.models.metric_upsert_request import MetricUpsertRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MetricUpsertRequest from a JSON string
metric_upsert_request_instance = MetricUpsertRequest.from_json(json)
# print the JSON string representation of the object
print(MetricUpsertRequest.to_json())

# convert the object into a dict
metric_upsert_request_dict = metric_upsert_request_instance.to_dict()
# create an instance of MetricUpsertRequest from a dict
metric_upsert_request_from_dict = MetricUpsertRequest.from_dict(metric_upsert_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


