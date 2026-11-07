# AccountDeviceListResponseMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** | Devices matching the filter. | 
**limit** | **int** |  | 
**offset** | **int** |  | 
**has_more** | **bool** |  | 
**next_offset** | **int** | Offset for the next page, or null on the last page. | 
**include_inactive** | **bool** |  | 

## Example

```python
from activitysmith_openapi.models.account_device_list_response_meta import AccountDeviceListResponseMeta

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDeviceListResponseMeta from a JSON string
account_device_list_response_meta_instance = AccountDeviceListResponseMeta.from_json(json)
# print the JSON string representation of the object
print(AccountDeviceListResponseMeta.to_json())

# convert the object into a dict
account_device_list_response_meta_dict = account_device_list_response_meta_instance.to_dict()
# create an instance of AccountDeviceListResponseMeta from a dict
account_device_list_response_meta_from_dict = AccountDeviceListResponseMeta.from_dict(account_device_list_response_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


