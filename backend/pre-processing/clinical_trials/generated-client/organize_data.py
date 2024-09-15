import json
import numpy as np
import pandas as pd



with open('NSCLC.json','r') as json_file:
    data = json.load(json_file) # write-in json file

assert isinstance(data, dict)


_, studieslist_raw = list(data.items())

studies = studieslist_raw[1]


df = pd.DataFrame()

data_rows = []

for s in studies[:5]:
    for k, v in s.items():
        print(k, v)

for s in studies:
    # try:
    #     ID = s['protocolSection']['identificationModule']['nctId']
    #     TITLE = s['protocolSection']['identificationModule']['briefTitle']
    #     CRITERIA = s['protocolSection']['eligibilityModule']['eligibilityCriteria']
    #     SEX = s['protocolSection']['eligibilityModule']['sex']
    #     AGE_MIN = int(s['protocolSection']['eligibilityModule'].get('minimumAge', "0 Years").split()[0])
    #     AGE_MAX = int(s['protocolSection']['eligibilityModule'].get('maximumAge', "200 Years").split()[0])
    #     EMAIL_DEFAULT = s['contactsLocationsModule']['centralContacts'][0]['email']

    #     substudies = s['contactsLocationsModule']['locations']
    #     sscounter = 0
    #     for ss in substudies:
    #         if ss['status'] == 'RECRUITING':
    #             if sscounter >= 100:
    #                 print("WRONG")
                
    #             SS_ID = ID[3:] + str(sscounter) if str(sscounter) == 2 else ID[3:] + "0" + str(sscounter)
    #             EMAIL = ss.get('contacts', EMAIL_DEFAULT) 
    #             GEO = (ss['geoPoint']['lat'], ss['geoPoint']['lon'])
    # except Exception as e:
    #     continue
    try:
        ID = s['protocolSection']['identificationModule']['nctId']
        TITLE = s['protocolSection']['identificationModule']['briefTitle']
        CRITERIA = s['protocolSection']['eligibilityModule']['eligibilityCriteria']
        SEX = s['protocolSection']['eligibilityModule']['sex']
        AGE_MIN = int(s['protocolSection']['eligibilityModule'].get('minimumAge', "0 Years").split()[0])
        AGE_MAX = int(s['protocolSection']['eligibilityModule'].get('maximumAge', "200 Years").split()[0])
        EMAIL_DEFAULT = s['protocolSection']['contactsLocationsModule']['centralContacts'][0]['email']

        substudies = s['protocolSection']['contactsLocationsModule']['locations']
        sscounter = 0
        for ss in substudies:
            try:
                sscounter += 1
                if ss['status'] == 'RECRUITING':
                    
                    SS_ID = ID[3:] + "0"*(3-len(str(sscounter))) + str(sscounter)
                    EMAIL = ss.get('contacts', EMAIL_DEFAULT) 
                    GEO = (ss['geoPoint']['lat'], ss['geoPoint']['lon'])
            except KeyError as e:
                sscounter -= 1
                continue


        data_rows.append({
            'TITLE': TITLE,
            'CRITERIA': CRITERIA,
            'SEX': SEX,
            'AGE_MIN': AGE_MIN,
            'AGE_MAX': AGE_MAX,
            'SS_ID': SS_ID,
            'EMAIL': EMAIL,
            'GEO': GEO
        })
    except KeyError as e:
        continue

df = pd.DataFrame(data_rows)

print(df)
df.to_json('flattened_data.json', orient='records')  # orient='records' exports each row as a dictionary

