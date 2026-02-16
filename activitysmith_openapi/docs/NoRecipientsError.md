# NoRecipientsError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 
**effective_channel_slugs** | **List[str]** |  | [optional] 

## Example

```python
from activitysmith_openapi.models.no_recipients_error import NoRecipientsError

# TODO update the JSON string below
json = "{}"
# create an instance of NoRecipientsError from a JSON string
no_recipients_error_instance = NoRecipientsError.from_json(json)
# print the JSON string representation of the object
print(NoRecipientsError.to_json())

# convert the object into a dict
no_recipients_error_dict = no_recipients_error_instance.to_dict()
# create an instance of NoRecipientsError from a dict
no_recipients_error_from_dict = NoRecipientsError.from_dict(no_recipients_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


