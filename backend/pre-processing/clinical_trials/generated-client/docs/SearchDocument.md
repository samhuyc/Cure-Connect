# SearchDocument


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**areas** | [**List[SearchArea]**](SearchArea.md) |  | 
**name** | **str** |  | 

## Example

```python
from openapi_client.models.search_document import SearchDocument

# TODO update the JSON string below
json = "{}"
# create an instance of SearchDocument from a JSON string
search_document_instance = SearchDocument.from_json(json)
# print the JSON string representation of the object
print(SearchDocument.to_json())

# convert the object into a dict
search_document_dict = search_document_instance.to_dict()
# create an instance of SearchDocument from a dict
search_document_from_dict = SearchDocument.from_dict(search_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


