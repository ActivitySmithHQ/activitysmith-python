# AccountDeviceListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**List[AccountDevice]**](AccountDevice.md) |  | 
**meta** | [**AccountDeviceListResponseMeta**](AccountDeviceListResponseMeta.md) |  | 

## Example

```python
from activitysmith_openapi.models.account_device_list_response import AccountDeviceListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDeviceListResponse from a JSON string
account_device_list_response_instance = AccountDeviceListResponse.from_json(json)
# print the JSON string representation of the object
print(AccountDeviceListResponse.to_json())

# convert the object into a dict
account_device_list_response_dict = account_device_list_response_instance.to_dict()
# create an instance of AccountDeviceListResponse from a dict
account_device_list_response_from_dict = AccountDeviceListResponse.from_dict(account_device_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


