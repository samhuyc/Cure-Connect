# FieldValuesStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**top_values** | [**List[ValueCount]**](ValueCount.md) |  | [optional] 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 
**unique_values_count** | **int** |  | 
**longest** | [**LongestString**](LongestString.md) |  | [optional] 
**formats** | **List[str]** |  | 
**max** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**avg** | **float** |  | [optional] 
**false_count** | **int** |  | 
**true_count** | **int** |  | 

## Example

```python
from openapi_client.models.field_values_stats import FieldValuesStats

# TODO update the JSON string below
json = "{}"
# create an instance of FieldValuesStats from a JSON string
field_values_stats_instance = FieldValuesStats.from_json(json)
# print the JSON string representation of the object
print(FieldValuesStats.to_json())

# convert the object into a dict
field_values_stats_dict = field_values_stats_instance.to_dict()
# create an instance of FieldValuesStats from a dict
field_values_stats_from_dict = FieldValuesStats.from_dict(field_values_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


