# DateStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | 
**formats** | **List[str]** |  | 
**max** | **str** |  | [optional] 
**min** | **str** |  | [optional] 
**missing_studies_count** | **int** |  | 
**piece** | **str** |  | 
**type** | [**FieldStatsType**](FieldStatsType.md) |  | 

## Example

```python
from openapi_client.models.date_stats import DateStats

# TODO update the JSON string below
json = "{}"
# create an instance of DateStats from a JSON string
date_stats_instance = DateStats.from_json(json)
# print the JSON string representation of the object
print(DateStats.to_json())

# convert the object into a dict
date_stats_dict = date_stats_instance.to_dict()
# create an instance of DateStats from a dict
date_stats_from_dict = DateStats.from_dict(date_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


