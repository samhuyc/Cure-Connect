# StringStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**longest** | [**LongestString**](LongestString.md) |  | [optional] 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**top_values** | [**List[ValueCount]**](ValueCount.md) |  | [optional] 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 
**unique_values_count** | **int** |  | 

## Example

```python
from openapi_client.models.string_stats import StringStats

# TODO update the JSON string below
json = "{}"
# create an instance of StringStats from a JSON string
string_stats_instance = StringStats.from_json(json)
# print the JSON string representation of the object
print(StringStats.to_json())

# convert the object into a dict
string_stats_dict = string_stats_instance.to_dict()
# create an instance of StringStats from a dict
string_stats_from_dict = StringStats.from_dict(string_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


