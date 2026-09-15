# ChangelogListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changelogs** | [**List[ChangelogEntry]**](ChangelogEntry.md) |  | 

## Example

```python
from activitysmith_openapi.models.changelog_list_response import ChangelogListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ChangelogListResponse from a JSON string
changelog_list_response_instance = ChangelogListResponse.from_json(json)
# print the JSON string representation of the object
print(ChangelogListResponse.to_json())

# convert the object into a dict
changelog_list_response_dict = changelog_list_response_instance.to_dict()
# create an instance of ChangelogListResponse from a dict
changelog_list_response_from_dict = ChangelogListResponse.from_dict(changelog_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


