# UpdateAppIconBadgeCount422Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **str** |  | 
**message** | **str** |  | 
**effective_channel_slugs** | **List[str]** |  | [optional] 
**code** | **str** |  | 
**badge** | **int** |  | 
**devices_targeted** | **int** |  | [optional] 
**devices_updated** | **int** |  | 
**users_updated** | **int** |  | [optional] 
**devices_notified** | **int** | Deprecated compatibility alias for devices_updated. | [optional] 

## Example

```python
from activitysmith_openapi.models.update_app_icon_badge_count422_response import UpdateAppIconBadgeCount422Response

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateAppIconBadgeCount422Response from a JSON string
update_app_icon_badge_count422_response_instance = UpdateAppIconBadgeCount422Response.from_json(json)
# print the JSON string representation of the object
print(UpdateAppIconBadgeCount422Response.to_json())

# convert the object into a dict
update_app_icon_badge_count422_response_dict = update_app_icon_badge_count422_response_instance.to_dict()
# create an instance of UpdateAppIconBadgeCount422Response from a dict
update_app_icon_badge_count422_response_from_dict = UpdateAppIconBadgeCount422Response.from_dict(update_app_icon_badge_count422_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


