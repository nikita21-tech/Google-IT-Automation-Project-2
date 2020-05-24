import os
import requests
import json
path = "/data/feedback/"
dirs = os.listdir( path )
for item in dirs:
    temp={}
    name = ['title', 'name', 'date', 'feedback']
    i = 0
    with open(path+item) as f :
        lines = f.readlines()
    for i in range(len(name)):
        temp[name[i]]=lines[i].rstrip("\n")
    data=json.dumps(temp)
    headers = {'Content-type': 'application/json'}
    response = requests.post("http://35.232.135.200/feedback/", data=data,headers=headers)
    print("status_code "+ str(response.status_code))
