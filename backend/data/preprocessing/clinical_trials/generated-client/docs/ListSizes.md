# ListSizes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**max_size** | **int** |  | [optional] 
**min_size** | **int** |  | [optional] 
**piece** | **str** |  | 
**top_sizes** | [**List[ListSize]**](ListSize.md) |  | [optional] 
**unique_sizes_count** | **int** |  | 

## Example

```python
from openapi_client.models.list_sizes import ListSizes

# TODO update the JSON string below
json = "{}"
# create an instance of ListSizes from a JSON string
list_sizes_instance = ListSizes.from_json(json)
# print the JSON string representation of the object
print(ListSizes.to_json())

# convert the object into a dict
list_sizes_dict = list_sizes_instance.to_dict()
# create an instance of ListSizes from a dict
list_sizes_from_dict = ListSizes.from_dict(list_sizes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


