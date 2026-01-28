# LiveActivityUpdateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**activity_id** | **str** |  | 
**devices_queued** | **int** |  | [optional] 
**devices_notified** | **int** |  | [optional] 
**timestamp** | **datetime** |  | 

## Example

```python
from openapi_client.models.live_activity_update_response import LiveActivityUpdateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityUpdateResponse from a JSON string
live_activity_update_response_instance = LiveActivityUpdateResponse.from_json(json)
# print the JSON string representation of the object
print(LiveActivityUpdateResponse.to_json())

# convert the object into a dict
live_activity_update_response_dict = live_activity_update_response_instance.to_dict()
# create an instance of LiveActivityUpdateResponse from a dict
live_activity_update_response_from_dict = LiveActivityUpdateResponse.from_dict(live_activity_update_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


