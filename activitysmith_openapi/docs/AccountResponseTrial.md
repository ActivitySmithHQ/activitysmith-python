# AccountResponseTrial

The trial while plan.status is trial, otherwise null. Time trials have ends_at and days_left. Older event trials have events_used and event_limit.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**ends_at** | **datetime** | When a time trial ends. | [optional] 
**days_left** | **int** | Days left in a time trial. 0 after it ends. | [optional] 
**events_used** | **int** | Events used in an event trial. | [optional] 
**event_limit** | **int** | Events included in an event trial. | [optional] 
**ended** | **bool** | True when the trial has ended or its events are used up. | 

## Example

```python
from activitysmith_openapi.models.account_response_trial import AccountResponseTrial

# TODO update the JSON string below
json = "{}"
# create an instance of AccountResponseTrial from a JSON string
account_response_trial_instance = AccountResponseTrial.from_json(json)
# print the JSON string representation of the object
print(AccountResponseTrial.to_json())

# convert the object into a dict
account_response_trial_dict = account_response_trial_instance.to_dict()
# create an instance of AccountResponseTrial from a dict
account_response_trial_from_dict = AccountResponseTrial.from_dict(account_response_trial_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


