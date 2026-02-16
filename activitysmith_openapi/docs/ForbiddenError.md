# ForbiddenError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from activitysmith_openapi.models.forbidden_error import ForbiddenError

# TODO update the JSON string below
json = "{}"
# create an instance of ForbiddenError from a JSON string
forbidden_error_instance = ForbiddenError.from_json(json)
# print the JSON string representation of the object
print(ForbiddenError.to_json())

# convert the object into a dict
forbidden_error_dict = forbidden_error_instance.to_dict()
# create an instance of ForbiddenError from a dict
forbidden_error_from_dict = ForbiddenError.from_dict(forbidden_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


