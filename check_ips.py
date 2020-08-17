#!/usr/bin/env python3
import requests
import sys

if (len(sys.argv) != 2):
    print("Usage: ./check_ips.py <NUMBER_OF_TEAMS>")
    exit(-1)

headers = {'Authorization': 'Basic OjEyMzQ='}
data = {"sploit": "", "team": "", "flag": "", "time-since": "", "time-until": "", "status": "",
        "checksystem_response": "", "page-number": "1", 'Authorization': 'Basic OjEyMzQ='}

f = open("ips.py", "w")
f.write("ips = {")

flag = False

#N is number of teams
N = int(sys.argv[1])
for i in range(1, N):
    for j in range(129, 151):  # First number is ip of the 1st VPN config and second number of last
        addr = f'6.6.{i}.{j}'
        print(addr)
        try:
            r = requests.get("http://" + addr + ":5000", headers=headers, data=data, timeout=5)
        except:
            continue
        print("http://" + addr + ":5000", r)
        if r.status_code == 200:
            addr = "'" + addr + "'"
            f.write("," + addr if flag else addr)
            flag = True

f.write("}")
f.close()



