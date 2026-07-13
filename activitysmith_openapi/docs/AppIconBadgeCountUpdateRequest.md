# AppIconBadgeCountUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**badge** | **int** | The count to show on the ActivitySmith app icon. Send 0 to clear it. | 
**target** | [**ChannelTarget**](ChannelTarget.md) |  | [optional] 

## Example

```python
from activitysmith_openapi.models.app_icon_badge_count_update_request import AppIconBadgeCountUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AppIconBadgeCountUpdateRequest from a JSON string
app_icon_badge_count_update_request_instance = AppIconBadgeCountUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AppIconBadgeCountUpdateRequest.to_json())

# convert the object into a dict
app_icon_badge_count_update_request_dict = app_icon_badge_count_update_request_instance.to_dict()
# create an instance of AppIconBadgeCountUpdateRequest from a dict
app_icon_badge_count_update_request_from_dict = AppIconBadgeCountUpdateRequest.from_dict(app_icon_badge_count_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


