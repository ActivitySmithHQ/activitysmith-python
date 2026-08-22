# AppIconBadgeCountUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**badge** | **int** |  | 
**devices_updated** | **int** | Number of devices whose App Icon Badge Count was updated. | 
**users_updated** | **int** | Number of account users with at least one updated device. | 
**devices_notified** | **int** | Deprecated compatibility alias for devices_updated. | [optional] 
**users_notified** | **int** | Deprecated compatibility alias for users_updated. | [optional] 
**effective_channel_slugs** | **List[str]** |  | 
**timestamp** | **datetime** |  | 

## Example

```python
from activitysmith_openapi.models.app_icon_badge_count_update_response import AppIconBadgeCountUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AppIconBadgeCountUpdateResponse from a JSON string
app_icon_badge_count_update_response_instance = AppIconBadgeCountUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(AppIconBadgeCountUpdateResponse.to_json())

# convert the object into a dict
app_icon_badge_count_update_response_dict = app_icon_badge_count_update_response_instance.to_dict()
# create an instance of AppIconBadgeCountUpdateResponse from a dict
app_icon_badge_count_update_response_from_dict = AppIconBadgeCountUpdateResponse.from_dict(app_icon_badge_count_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


