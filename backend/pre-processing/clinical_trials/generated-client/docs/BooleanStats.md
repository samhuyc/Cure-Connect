# BooleanStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**false_count** | **int** |  | 
**var_field** | **str** |  | 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**true_count** | **int** |  | 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 

## Example

```python
from openapi_client.models.boolean_stats import BooleanStats

# TODO update the JSON string below
json = "{}"
# create an instance of BooleanStats from a JSON string
boolean_stats_instance = BooleanStats.from_json(json)
# print the JSON string representation of the object
print(BooleanStats.to_json())

# convert the object into a dict
boolean_stats_dict = boolean_stats_instance.to_dict()
# create an instance of BooleanStats from a dict
boolean_stats_from_dict = BooleanStats.from_dict(boolean_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


