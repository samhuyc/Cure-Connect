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
    fields = ['NCTId', 'BriefTitle', 'EligibilityModule', 'LocationStatus', 'LocationContactEMail', 'LocationGeoPoint', 'CentralContactEMail'] # or Location
    filter_overall_status = ["RECRUITING"]
    query_cond = "non-small cell lung cancer"
    # fields = ['[\"NCTId\",\"BriefTitle\",\"OverallStatus\",\"HasResults\"]']

try:
    # Fetch Studies
    api_response = api_instance.list_studies(fields=fields, query_cond=query_cond, filter_overall_status=filter_overall_status, page_size=1000)

    # Store json
    with open('NSCLC.json', 'w') as json_file:
        json_file.write(api_response.to_json())

    print("done")
    
    # api_response_dict = api_response.to_dict() if hasattr(api_response, "to_dict") else api_response
    # # print(len(api_response_dict))
    # for k, protocol in api_response_dict.items():
    #     for study in protocol:
    #         print(study)
    #         print("\n")
    #         print("*"*100)

except Exception as e:
    print("Exception when calling StudiesApi->list_studies: %s\n" % e)
