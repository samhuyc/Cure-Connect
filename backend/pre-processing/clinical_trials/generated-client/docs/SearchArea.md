# SearchArea


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**param** | **str** |  | [optional] 
**parts** | [**List[SearchPart]**](SearchPart.md) |  | 
**ui_label** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.search_area import SearchArea

# TODO update the JSON string below
json = "{}"
# create an instance of SearchArea from a JSON string
search_area_instance = SearchArea.from_json(json)
# print the JSON string representation of the object
print(SearchArea.to_json())

# convert the object into a dict
search_area_dict = search_area_instance.to_dict()
# create an instance of SearchArea from a dict
search_area_from_dict = SearchArea.from_dict(search_area_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


