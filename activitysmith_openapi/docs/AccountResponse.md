# AccountResponse

The account's plan and trial, and whether sends go through.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | Email of the signed-in person. Null for API keys. | 
**is_account_owner** | **bool** | True when the signed-in person owns the account. Null for API keys. | 
**plan** | [**AccountResponsePlan**](AccountResponsePlan.md) |  | 
**trial** | [**AccountResponseTrial**](AccountResponseTrial.md) |  | 
**can_send** | **bool** | False when Push Notifications, Live Activities, App Icon Badge updates, and Lock Screen Widget values are paused until the account upgrades. | 
**when_trial_ends** | **str** | What stops when the trial ends. Present only while a trial is running. | [optional] 
**upgrade_url** | **str** | Where to upgrade. Set during a trial or without an active plan, otherwise null. | 

## Example

```python
from activitysmith_openapi.models.account_response import AccountResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponse from a JSON string
account_response_instance = AccountResponse.from_json(json)
# print the JSON string representation of the object
print(AccountResponse.to_json())

# convert the object into a dict
account_response_dict = account_response_instance.to_dict()
# create an instance of AccountResponse from a dict
account_response_from_dict = AccountResponse.from_dict(account_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


