# EnumItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exceptions** | **object** |  | [optional] 
**legacy_value** | **str** |  | 
**value** | **str** |  | 

## Example

```python
from openapi_client.models.enum_item import EnumItem

# TODO update the JSON string below
json = "{}"
# create an instance of EnumItem from a JSON string
enum_item_instance = EnumItem.from_json(json)
# print the JSON string representation of the object
print(EnumItem.to_json())

# convert the object into a dict
enum_item_dict = enum_item_instance.to_dict()
# create an instance of EnumItem from a dict
enum_item_from_dict = EnumItem.from_dict(enum_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


