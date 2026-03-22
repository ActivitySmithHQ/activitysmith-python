# ActivityMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | 
**value** | **float** |  | 
**unit** | **str** |  | [optional] 

## Example

```python
from activitysmith_openapi.models.activity_metric import ActivityMetric

# TODO update the JSON string below
json = "{}"
# create an instance of ActivityMetric from a JSON string
activity_metric_instance = ActivityMetric.from_json(json)
# print the JSON string representation of the object
print(ActivityMetric.to_json())

# convert the object into a dict
activity_metric_dict = activity_metric_instance.to_dict()
# create an instance of ActivityMetric from a dict
activity_metric_from_dict = ActivityMetric.from_dict(activity_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


