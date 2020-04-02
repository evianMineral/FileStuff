import http.client
import mimetypes
import pandas as pd
import json

conn = http.client.HTTPSConnection("api.hubapi.com")
payload = ''
headers = {
  'Authorization': 'Bearer CIibr-2RLhICAQEYxPC9AyDize8EKOmODTIZAGSzfscq259QY307K8zbooR6vnD3nhaE7zoPAAoCQQAADIADAAgAAAABQhkAZLN-xyUb4paOmzC6tyzvqadgIVL3jNAZ',
  'Cookie': '__cfduid=d74edea36dd6557df79148c61f7e0da171585233082'
}
conn.request("GET", "/contacts/v1/lists/all/contacts/all", payload, headers)
res = conn.getresponse()
data = res.read()
#print(data.decode("utf-8"))
df = pd.read_json(data)

test = json.loads(data)
contact1 = test['contacts'][0]
property1 = contact1['properties']
contact2 = test['contacts'][1]
property2 = ['properties']

localDico = []
localDico.append(contact1)
localDico.append(contact2)

df = pd.DataFrame.from_dict(localDico)

print(df)