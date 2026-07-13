# LiveActivityStreamRequest

Send the latest state for a managed Live Activity stream. channels is the streamlined form for stream targeting. target.channels is also accepted for compatibility. If both are provided, they must match.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content_state** | [**StreamContentState**](StreamContentState.md) |  | 
**action** | [**LiveActivityAction**](LiveActivityAction.md) |  | [optional] 
**secondary_action** | [**LiveActivityAction**](LiveActivityAction.md) | Optional secondary action button. Supported for alert, progress, and segmented_progress Live Activities. Uses the same open_url, shortcuts://, and webhook shapes as action. | [optional] 
**alert** | [**AlertPayload**](AlertPayload.md) |  | [optional] 
**channels** | **List[str]** | Channel slugs. When omitted, API key scope determines recipients. | [optional] 
**target** | [**ChannelTarget**](ChannelTarget.md) |  | [optional] 

## Example

```python
from activitysmith_openapi.models.live_activity_stream_request import LiveActivityStreamRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LiveActivityStreamRequest from a JSON string
live_activity_stream_request_instance = LiveActivityStreamRequest.from_json(json)
# print the JSON string representation of the object
print(LiveActivityStreamRequest.to_json())

# convert the object into a dict
live_activity_stream_request_dict = live_activity_stream_request_instance.to_dict()
# create an instance of LiveActivityStreamRequest from a dict
live_activity_stream_request_from_dict = LiveActivityStreamRequest.from_dict(live_activity_stream_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


