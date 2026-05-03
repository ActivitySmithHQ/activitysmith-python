# WidgetMetric

A metric configured for ActivitySmith widgets.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public_id** | **str** |  | 
**key** | **str** |  | 
**label** | **str** |  | 
**currency_code** | **str** | Present when format is currency. | 
**unit** | **str** | Present when format is unit. | 
**unit_spacing** | [**MetricUnitSpacing**](MetricUnitSpacing.md) |  | 
**format** | [**MetricFormat**](MetricFormat.md) |  | 
**latest_value** | **float** | Latest metric value. Numeric formats return a number. String metrics return text. | 
**latest_value_at** | **datetime** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.widget_metric import WidgetMetric

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetMetric from a JSON string
widget_metric_instance = WidgetMetric.from_json(json)
# print the JSON string representation of the object
print(WidgetMetric.to_json())

# convert the object into a dict
widget_metric_dict = widget_metric_instance.to_dict()
# create an instance of WidgetMetric from a dict
widget_metric_from_dict = WidgetMetric.from_dict(widget_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


