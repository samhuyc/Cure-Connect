# IntegerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** |  | [optional] 
**var_field** | **str** |  | 
**max** | **int** |  | [optional] 
**min** | **int** |  | [optional] 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 

## Example

```python
from openapi_client.models.integer_stats import IntegerStats

# TODO update the JSON string below
json = "{}"
# create an instance of IntegerStats from a JSON string
integer_stats_instance = IntegerStats.from_json(json)
# print the JSON string representation of the object
print(IntegerStats.to_json())

# convert the object into a dict
integer_stats_dict = integer_stats_instance.to_dict()
# create an instance of IntegerStats from a dict
integer_stats_from_dict = IntegerStats.from_dict(integer_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


