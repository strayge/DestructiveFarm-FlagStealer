#!/usr/bin/env python3
import requests
import json

headers = {
    'Authorization': 'Basic OjEyMzQ=',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}
data = {
    "sploit": "",
    "team": "",
    "flag": "",
    "time-since": "",
    "time-until": "",
    "status": "",
    "checksystem_response": "",
    "page-number": "1",
}

result = {}

def save():
    with open('ip.json', 'wt') as f:
        json.dump(result, f)

if __name__ == '__main__':
    for team_num in range(1, 50 + 1):
        for client_ip in range(128, 254 + 1):
            ip = f'6.6.{team_num}.{client_ip}'
            try:
                r = requests.get(f'http://{ip}:5000', headers=headers, data=data, timeout=3)
                result[ip] = r.status_code
                print(f'{ip}: {r.status_code}')
                save()
            except Exception as e:
                print(f'{ip}: {type(e).__name__}')
