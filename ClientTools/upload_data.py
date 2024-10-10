import requests
import json
import csv

def request_api(url,row_data):
    ret = []
    #url = URL_ROOT+'v1/devices/borrow/'
    headers = {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjQ5Nzc0OTYwLCJlbWFpbCI6ImFkbWluQHRlc3QuMTIzIn0.i3Br9X0-11SSsABh0-YXPVomfRrX1MVpo3LiIqUOfCE',
        #'Content-Type': 'multipart/form-data'
    }
    time_b,time_e = create_time(row_data[1])

    data = {
        'remark': row_data[4],
        'reason': row_data[2],
        'device': row_data[0],
        'user': row_data[3],
        'time_borrowed': time_b,
        'is_return': True if time_e != 'None' else False
    }
    if time_e != 'None':
        data['time_end'] = time_e

    response = requests.post(url=url,
    data = data,
    headers=headers)

    print(repr(response.text))
    ret.append(response.status_code)
    print(len(ret))

def create_time(t_str):

    sprate = t_str.split(' - ')
    time_b = sprate[0].replace('.','-')+'T00:00:00.000-0200'
    time_e = sprate[1].replace('.','-')+'T00:00:00.000-0300' if sprate[1] != '#' else 'None'
    print(time_b,time_e)
    return time_b,time_e

def main():
    with open('/users/luther/documents/data.csv','r') as f:

        reader = csv.reader(f)
        count = 0
        for row in reader:
            print(row)
            count += 1
            request_api(row)
        print(count)

if __name__ == '__main__':
    main()