# EnumInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pieces** | **List[str]** |  | 
**type** | **str** |  | 
**values** | [**List[EnumItem]**](EnumItem.md) |  | 

## Example

```python
from openapi_client.models.enum_info import EnumInfo

# TODO update the JSON string below
json = "{}"
# create an instance of EnumInfo from a JSON string
enum_info_instance = EnumInfo.from_json(json)
# print the JSON string representation of the object
print(EnumInfo.to_json())

# convert the object into a dict
enum_info_dict = enum_info_instance.to_dict()
# create an instance of EnumInfo from a dict
enum_info_from_dict = EnumInfo.from_dict(enum_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


