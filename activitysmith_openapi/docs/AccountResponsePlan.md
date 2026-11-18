# AccountResponsePlan


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | trial: the free trial. subscription: a monthly or yearly plan. lifetime: a Lifetime Membership. grandfathered: an early account with free access. inactive: no trial and no active plan. | 
**plan_id** | **str** | Plan ID, such as pro. Null during a trial or without a plan. | 
**billing_interval** | **str** | month or year for subscriptions, otherwise null. | 
**renews_at** | **datetime** | Next payment date of a subscription, otherwise null. | 
**cancel_at_period_end** | **bool** | True when the subscription ends at the end of the current period. | 

## Example

```python
from activitysmith_openapi.models.account_response_plan import AccountResponsePlan

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponsePlan from a JSON string
account_response_plan_instance = AccountResponsePlan.from_json(json)
# print the JSON string representation of the object
print(AccountResponsePlan.to_json())

# convert the object into a dict
account_response_plan_dict = account_response_plan_instance.to_dict()
# create an instance of AccountResponsePlan from a dict
account_response_plan_from_dict = AccountResponsePlan.from_dict(account_response_plan_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


