# LiveActivityEndResponse


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
from activitysmith.models.live_activity_end_response import LiveActivityEndResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityEndResponse from a JSON string
live_activity_end_response_instance = LiveActivityEndResponse.from_json(json)
# print the JSON string representation of the object
print(LiveActivityEndResponse.to_json())

# convert the object into a dict
live_activity_end_response_dict = live_activity_end_response_instance.to_dict()
# create an instance of LiveActivityEndResponse from a dict
live_activity_end_response_from_dict = LiveActivityEndResponse.from_dict(live_activity_end_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


