# ChangelogItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon** | **str** |  | [optional] 
**title** | **str** |  | 
**body** | **str** |  | 
**image_url** | **str** |  | [optional] 
**accent_color** | **str** |  | [optional] 

## Example

```python
from activitysmith_openapi.models.changelog_item import ChangelogItem

# TODO update the JSON string below
json = "{}"
# create an instance of ChangelogItem from a JSON string
changelog_item_instance = ChangelogItem.from_json(json)
# print the JSON string representation of the object
print(ChangelogItem.to_json())

# convert the object into a dict
changelog_item_dict = changelog_item_instance.to_dict()
# create an instance of ChangelogItem from a dict
changelog_item_from_dict = ChangelogItem.from_dict(changelog_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


