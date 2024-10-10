import requests
import json
import csv

URL_ROOT = 'http://assets.uat.enflame.cc/api/v1/devices/device/'
def request_api(row_data):
    ret = []
    url = URL_ROOT
    print(url)
    headers = {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg3OTk4NjA2LCJlbWFpbCI6ImFkbWluQHRlc3QuMTIzIn0.IGxzM3aL0jH2XbE42CeDH9VG9v5ggfUi1RCTdtgOOO8',
    }
    nm = row_data[2].split('-')[1]
    data = {
        'name': row_data[0],
        'type': row_data[1],
        'hostname': 'cse-ws-' + nm,
        'sn': row_data[2],
        'number': row_data[2],
        'ip': row_data[2],
        'account': row_data[3],
       
    }
    

    response = requests.post(url=url,
    data = data,
    headers=headers)
    print(response.status_code)
    ret.append(response.status_code)
    print(len(ret))

def main():
    with open(r'c:\Users\luther.wu\Downloads\server.csv','r',encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        count = 0
        for row in reader:
            print(row)
            count += 1
            request_api(row)
        print(count)

if __name__ == '__main__':
    main()