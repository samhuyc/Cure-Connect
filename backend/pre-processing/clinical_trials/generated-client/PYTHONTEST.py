import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint
import json

# Defining the host is optional and defaults to https://clinicaltrials.gov/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://clinicaltrials.gov/api/v2"
)




with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.StudiesApi(api_client)
    # fields = ['NCTId', 'BriefTitle', ]
    fields = ['NCTId', 'BriefTitle', 'EligibilityModule', 'LocationGeoPoint', 'LocationContactEMail'] # or Location
    filter_overall_status = ["RECRUITING"]
    query_cond = "non-small cell lung cancer"
    # fields = ['[\"NCTId\",\"BriefTitle\",\"OverallStatus\",\"HasResults\"]']

try:
    # Studies
    api_response = api_instance.list_studies(fields=fields, query_cond=query_cond, filter_overall_status=filter_overall_status, page_size=1000)
    print("\n")
    
    # Convert to dict if available
    api_response_dict = api_response.to_dict() if hasattr(api_response, "to_dict") else api_response
    
    # print(type(api_response_dict))
    # Process the dictionary
    for k, v in api_response_dict.items():
        for study in v:
            print(study)
            print()

except Exception as e:
    print("Exception when calling StudiesApi->list_studies: %s\n" % e)

# try:
#     # Studies
#     api_response = api_instance.list_studies(fields = fields, query_cond=query_cond, filter_overall_status=filter_overall_status, page_size=1000)
#     print("The response of StudiesApi->list_studies:\n")
#     pprint(api_response)

# except Exception as e:
#     print("Exception when calling StudiesApi->list_studies: %s\n" % e)

# '''
# instance of looking up a study by NCT number
# '''
# # Enter a context with an instance of the API client
# with openapi_client.ApiClient(configuration) as api_client:
#     # Create an instance of the API class
#     api_instance = openapi_client.StudiesApi(api_client)
#     nct_id = 'NCT00841061' # str | NCT Number of a study. If found in [NCTIdAlias](data-api/about-api/study-data-structure#NCTIdAlias) field, 301 HTTP redirect to the actual study will be returned.
#     # nct_id = '' 
#     format = "json" # str | Must be one of the following: * `csv`- return CSV table; available fields are listed on [CSV Download](/data-api/about-api/csv-download) * `json`- return JSON object; format of `markup` fields depends on `markupFormat` parameter * `json.zip`- put JSON object into a .json file and download it as zip archive; field values of type `markup` are in [markdown](https://spec.commonmark.org/0.28/) format * `fhir.json` - return FHIR JSON; fields are not customizable; see [Access Data in FHIR](/data-api/fhir) * `ris`- return RIS record; available tags are listed on [RIS Download](/data-api/about-api/ris-download) (optional) (default to json)
#     markup_format = "markdown" # str | Format of `markup` type fields: * `markdown`- [markdown](https://spec.commonmark.org/0.28/) format * `legacy`- compatible with classic PRS  Applicable only to `json` format. (optional) (default to markdown)
#     fields = ['[\"NCTId\",\"BriefTitle\",\"Reference\"]'] # List[str] | If specified, must be non-empty comma- or pipe-separated list of fields to return. If unspecified, all fields will be returned. Order of the fields does not matter.  For `csv` format, specify list of columns. The column names are available on [CSV Download](/data-api/about-api/csv-download).  For `json` and `json.zip` formats, every list item is either area name, piece name, or field name. If a piece or a field is a branch node, all descendant fields will be included. All area names are available on [Search Areas](/data-api/about-api/search-areas), the piece and field names - on [Data Structure](/data-api/about-api/study-data-structure) and also can be retrieved at `/studies/metadata` endpoint.  For `fhir.json` format, all available fields are returned and this parameter must be unspecified.  For `ris` format, specify list of tags. The tag names are available on [RIS Download](/data-api/about-api/ris-download). (optional)

#     try:
#         # Single Study
#         # api_response = api_instance.fetch_study(nct_id, format=format, markup_format=markup_format, fields=fields)
#         api_response = api_instance.fetch_study(nct_id, format=format, markup_format=markup_format)
#         print("The response of StudiesApi->fetch_study:\n")
#         pprint(api_response)
#     except Exception as e:
#         print("Exception when calling StudiesApi->fetch_study: %s\n" % e)