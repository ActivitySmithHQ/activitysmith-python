# AccountDevice

An iPhone or iPad paired to the account, one entry per device and owner.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_email** | **str** | Email of the account member who paired the device. | 
**device_id** | **str** | Device ID. Use it to assign the device to Channels. | 
**device_type** | **str** | Device platform, such as ios. iPhones and iPads both report ios; use system_name to tell them apart. | 
**is_active** | **bool** | True when the device can receive Push Notifications or Live Activities. | 
**token_status** | **Dict[str, bool]** | Whether each delivery token is active, keyed by token type (push, start_live_activity). | 
**app_version** | **str** | ActivitySmith app version on the device. | 
**device_name** | **str** | Device name set on the device. | 
**system_name** | **str** | Operating system name, such as iOS or iPadOS. | 
**system_version** | **str** | Operating system version. | 
**created_at** | **datetime** | When the device was first paired. | 
**updated_at** | **datetime** | When the device last updated its pairing. | 

## Example

```python
from activitysmith_openapi.models.account_device import AccountDevice

# TODO update the JSON string below
json = "{}"
# create an instance of AccountDevice from a JSON string
account_device_instance = AccountDevice.from_json(json)
# print the JSON string representation of the object
print(AccountDevice.to_json())

# convert the object into a dict
account_device_dict = account_device_instance.to_dict()
# create an instance of AccountDevice from a dict
account_device_from_dict = AccountDevice.from_dict(account_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


