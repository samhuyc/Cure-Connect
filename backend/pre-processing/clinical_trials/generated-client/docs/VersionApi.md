# openapi_client.VersionApi

All URIs are relative to *https://clinicaltrials.gov/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version**](VersionApi.md#version) | **GET** /version | Version


# **version**
> Version version()

Version

API and data versions.  API version follows [Semantic Versioning 2.0.0 Schema](https://semver.org/spec/v2.0.0.html). Data version is UTC timestamp in `yyyy-MM-dd'T'HH:mm:ss` format.

### Example


```python
import openapi_client
from openapi_client.models.version import Version
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
    api_instance = openapi_client.VersionApi(api_client)

    try:
        # Version
        api_response = api_instance.version()
        print("The response of VersionApi->version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Version**](Version.md)

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

