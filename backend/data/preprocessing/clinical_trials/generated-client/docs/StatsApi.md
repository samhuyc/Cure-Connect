# openapi_client.StatsApi

All URIs are relative to *https://clinicaltrials.gov/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**field_values_stats**](StatsApi.md#field_values_stats) | **GET** /stats/field/values | Field Values
[**list_field_sizes_stats**](StatsApi.md#list_field_sizes_stats) | **GET** /stats/field/sizes | List Field Sizes
[**size_stats**](StatsApi.md#size_stats) | **GET** /stats/size | Study Sizes


# **field_values_stats**
> List[FieldValuesStats] field_values_stats(types=types, fields=fields)

Field Values

Value statistics of the study leaf fields.

### Example


```python
import openapi_client
from openapi_client.models.field_stats_type import FieldStatsType
from openapi_client.models.field_values_stats import FieldValuesStats
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://clinicaltrials.gov/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://clinicaltrials.gov/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatsApi(api_client)
    types = [] # List[FieldStatsType] | Filter by field types (optional) (default to [])
    fields = ['[\"Phase\"]'] # List[str] | Filter by piece names or field paths of leaf fields. See [Data Structure](/data-api/about-api/study-data-structure) for the available values.  If specified, must be non-empty comma- or pipe-separated list of fields to return. (optional)

    try:
        # Field Values
        api_response = api_instance.field_values_stats(types=types, fields=fields)
        print("The response of StatsApi->field_values_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->field_values_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **types** | [**List[FieldStatsType]**](FieldStatsType.md)| Filter by field types | [optional] [default to []]
 **fields** | [**List[str]**](str.md)| Filter by piece names or field paths of leaf fields. See [Data Structure](/data-api/about-api/study-data-structure) for the available values.  If specified, must be non-empty comma- or pipe-separated list of fields to return. | [optional] 

### Return type

[**List[FieldValuesStats]**](FieldValuesStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_field_sizes_stats**
> List[ListSizes] list_field_sizes_stats(fields=fields)

List Field Sizes

Sizes of list/array fields.  To search studies by a list field size, use `AREA[FieldName:size]` search operator. For example, [AREA\\[Phase:size\\] 2](https://clinicaltrials.gov/search?term=AREA%5BPhase:size%5D%202) query finds studies with 2 phases.

### Example


```python
import openapi_client
from openapi_client.models.list_sizes import ListSizes
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://clinicaltrials.gov/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://clinicaltrials.gov/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatsApi(api_client)
    fields = ['[\"Phase\"]'] # List[str] | Filter by piece names or field paths of leaf fields. See [Data Structure](/data-api/about-api/study-data-structure) for the available values.  If specified, must be non-empty comma- or pipe-separated list of fields to return. If unspecified, all available stats will be returned. (optional)

    try:
        # List Field Sizes
        api_response = api_instance.list_field_sizes_stats(fields=fields)
        print("The response of StatsApi->list_field_sizes_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->list_field_sizes_stats: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fields** | [**List[str]**](str.md)| Filter by piece names or field paths of leaf fields. See [Data Structure](/data-api/about-api/study-data-structure) for the available values.  If specified, must be non-empty comma- or pipe-separated list of fields to return. If unspecified, all available stats will be returned. | [optional] 

### Return type

[**List[ListSizes]**](ListSizes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |
**404** | Not Found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **size_stats**
> GzipStats size_stats()

Study Sizes

Statistics of study JSON sizes.

### Example


```python
import openapi_client
from openapi_client.models.gzip_stats import GzipStats
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://clinicaltrials.gov/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://clinicaltrials.gov/api/v2"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StatsApi(api_client)

    try:
        # Study Sizes
        api_response = api_instance.size_stats()
        print("The response of StatsApi->size_stats:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatsApi->size_stats: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GzipStats**](GzipStats.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

