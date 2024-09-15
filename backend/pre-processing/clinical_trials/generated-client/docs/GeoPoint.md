# GeoPoint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lat** | **float** |  | 
**lon** | **float** |  | 

## Example

```python
from openapi_client.models.geo_point import GeoPoint

# TODO update the JSON string below
json = "{}"
# create an instance of GeoPoint from a JSON string
geo_point_instance = GeoPoint.from_json(json)
# print the JSON string representation of the object
print(GeoPoint.to_json())

# convert the object into a dict
geo_point_dict = geo_point_instance.to_dict()
# create an instance of GeoPoint from a dict
geo_point_from_dict = GeoPoint.from_dict(geo_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


