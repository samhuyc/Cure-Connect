# GzipStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_size_bytes** | **int** |  | 
**largest_studies** | [**List[StudySize]**](StudySize.md) |  | 
**percentiles** | **object** |  | 
**ranges** | [**List[DistItem]**](DistItem.md) |  | 
**total_studies** | **int** |  | 

## Example

```python
from openapi_client.models.gzip_stats import GzipStats

# TODO update the JSON string below
json = "{}"
# create an instance of GzipStats from a JSON string
gzip_stats_instance = GzipStats.from_json(json)
# print the JSON string representation of the object
print(GzipStats.to_json())

# convert the object into a dict
gzip_stats_dict = gzip_stats_instance.to_dict()
# create an instance of GzipStats from a dict
gzip_stats_from_dict = GzipStats.from_dict(gzip_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


