# ChannelTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**channels** | **List[str]** | Channel slugs. When omitted, API key scope determines recipients. | 

## Example

```python
from activitysmith_openapi.models.channel_target import ChannelTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ChannelTarget from a JSON string
channel_target_instance = ChannelTarget.from_json(json)
# print the JSON string representation of the object
print(ChannelTarget.to_json())

# convert the object into a dict
channel_target_dict = channel_target_instance.to_dict()
# create an instance of ChannelTarget from a dict
channel_target_from_dict = ChannelTarget.from_dict(channel_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


