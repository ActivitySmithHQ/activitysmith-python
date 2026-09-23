# BillingBlockedError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 
**trial_period** | [**BillingBlockedErrorTrialPeriod**](BillingBlockedErrorTrialPeriod.md) |  | [optional] 
**upgrade_url** | **str** |  | 

## Example

```python
from activitysmith_openapi.models.billing_blocked_error import BillingBlockedError

# TODO update the JSON string below
json = "{}"
# create an instance of BillingBlockedError from a JSON string
billing_blocked_error_instance = BillingBlockedError.from_json(json)
# print the JSON string representation of the object
print(BillingBlockedError.to_json())

# convert the object into a dict
billing_blocked_error_dict = billing_blocked_error_instance.to_dict()
# create an instance of BillingBlockedError from a dict
billing_blocked_error_from_dict = BillingBlockedError.from_dict(billing_blocked_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


