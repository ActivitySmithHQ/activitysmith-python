# ChangelogEntry


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**platform** | **str** |  | 
**version** | **str** |  | 
**title** | **str** |  | 
**subtitle** | **str** |  | 
**hero_image_url** | **str** |  | 
**cta_title** | **str** |  | 
**published_at** | **datetime** |  | 
**items** | [**List[ChangelogItem]**](ChangelogItem.md) |  | 

## Example

```python
from activitysmith_openapi.models.changelog_entry import ChangelogEntry

# TODO update the JSON string below
json = "{}"
# create an instance of ChangelogEntry from a JSON string
changelog_entry_instance = ChangelogEntry.from_json(json)
# print the JSON string representation of the object
print(ChangelogEntry.to_json())

# convert the object into a dict
changelog_entry_dict = changelog_entry_instance.to_dict()
# create an instance of ChangelogEntry from a dict
changelog_entry_from_dict = ChangelogEntry.from_dict(changelog_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


