# AppIconBadgeCountUpdateError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**code** | **str** |  | 
**message** | **str** |  | 
**badge** | **int** |  | 
**devices_targeted** | **int** |  | [optional] 
**devices_updated** | **int** |  | 
**users_updated** | **int** |  | [optional] 
**devices_notified** | **int** | Deprecated compatibility alias for devices_updated. | [optional] 
**effective_channel_slugs** | **List[str]** |  | [optional] 

## Example

```python
from activitysmith_openapi.models.app_icon_badge_count_update_error import AppIconBadgeCountUpdateError

# TODO update the JSON string below
json = "{}"
# create an instance of AppIconBadgeCountUpdateError from a JSON string
app_icon_badge_count_update_error_instance = AppIconBadgeCountUpdateError.from_json(json)
# print the JSON string representation of the object
print(AppIconBadgeCountUpdateError.to_json())

# convert the object into a dict
app_icon_badge_count_update_error_dict = app_icon_badge_count_update_error_instance.to_dict()
# create an instance of AppIconBadgeCountUpdateError from a dict
app_icon_badge_count_update_error_from_dict = AppIconBadgeCountUpdateError.from_dict(app_icon_badge_count_update_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


