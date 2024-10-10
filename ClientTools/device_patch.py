import requests
import json
import csv

URL_ROOT = 'http://assets.uat.enflame.cc/api/v1/devices/device/'
def request_api(row_data):
    ret = []
    url = URL_ROOT+row_data[0]+'/'
    print(url)
    headers = {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg3OTk4NjA2LCJlbWFpbCI6ImFkbWluQHRlc3QuMTIzIn0.IGxzM3aL0jH2XbE42CeDH9VG9v5ggfUi1RCTdtgOOO8',
        #'Content-Type': 'multipart/form-data'
    }
    # time_b,time_e = create_time(row_data[1])
    nm = row_data[1].split('-')[1]
    data = {
        'hostname': 'cse-sv-' + nm,
        'sn': row_data[1],
        'number': row_data[1],
        'status': row_data[2],
        'locate': row_data[3],
        'config': row_data[4],
        'vender_type': row_data[5],
        # 'time_borrowed': time_b,
        # 'is_return': True if time_e != 'None' else False
    }
    # if time_e != 'None':
    #     data['time_end'] = time_e

    response = requests.patch(url=url,
    data = data,
    headers=headers)

    print(repr(response.text))
    print(response.status_code)
    ret.append(response.status_code)
    print(len(ret))

def create_time(t_str):

    sprate = t_str.split(' - ')
    time_b = sprate[0].replace('.','-')+'T00:00:00.000-0200'
    time_e = sprate[1].replace('.','-')+'T00:00:00.000-0300' if sprate[1] != '#' else 'None'
    print(time_b,time_e)
    return time_b,time_e

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