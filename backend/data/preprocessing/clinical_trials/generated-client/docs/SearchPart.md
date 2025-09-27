# SearchPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_enum** | **bool** |  | 
**is_synonyms** | **bool** |  | 
**pieces** | **List[str]** |  | 
**type** | **str** |  | 
**weight** | **float** |  | 

## Example

```python
from openapi_client.models.search_part import SearchPart

# TODO update the JSON string below
json = "{}"
# create an instance of SearchPart from a JSON string
search_part_instance = SearchPart.from_json(json)
# print the JSON string representation of the object
print(SearchPart.to_json())

# convert the object into a dict
search_part_dict = search_part_instance.to_dict()
# create an instance of SearchPart from a dict
search_part_from_dict = SearchPart.from_dict(search_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


