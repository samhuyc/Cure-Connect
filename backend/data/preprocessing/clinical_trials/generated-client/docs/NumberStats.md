# NumberStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**avg** | **float** |  | [optional] 
**var_field** | **str** |  | 
**max** | **float** |  | [optional] 
**min** | **float** |  | [optional] 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 

## Example

```python
from openapi_client.models.number_stats import NumberStats

# TODO update the JSON string below
json = "{}"
# create an instance of NumberStats from a JSON string
number_stats_instance = NumberStats.from_json(json)
# print the JSON string representation of the object
print(NumberStats.to_json())

# convert the object into a dict
number_stats_dict = number_stats_instance.to_dict()
# create an instance of NumberStats from a dict
number_stats_from_dict = NumberStats.from_dict(number_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


