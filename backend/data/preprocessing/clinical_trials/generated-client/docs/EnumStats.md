# EnumStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**top_values** | [**List[ValueCount]**](ValueCount.md) |  | [optional] 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 
**unique_values_count** | **int** |  | 

## Example

```python
from openapi_client.models.enum_stats import EnumStats

# TODO update the JSON string below
json = "{}"
# create an instance of EnumStats from a JSON string
enum_stats_instance = EnumStats.from_json(json)
# print the JSON string representation of the object
print(EnumStats.to_json())

# convert the object into a dict
enum_stats_dict = enum_stats_instance.to_dict()
# create an instance of EnumStats from a dict
enum_stats_from_dict = EnumStats.from_dict(enum_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


