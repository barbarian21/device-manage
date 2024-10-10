import requests
import json

def login(url,data):
    response = requests.post(url,data=data)
    if response.status_code == 200:
        j_res = json.loads(response.text)
        return j_res['token']
    else:
        return ''

if __name__ == '__main__':
    login('','','')