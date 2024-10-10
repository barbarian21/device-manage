import requests
import json

URL_ROOT = 'http://assets.uat.enflame.cc/api/'

def login(user,passwd):

    url = 'http://assets.uat.enflame.cc/api/login/'

    data = {
        'username': user,
        'password': passwd
    }

    response = requests.post(url,data=data)
    print(repr(response.text))
    j_res = json.loads(response.text)
    print(repr(j_res))

    return j_res['token']


def request_api(sn):
    res_status = []
    url = URL_ROOT+'v1/cards/card/eb2e85a8-753c-4d5b-a7b0-ffc346d22682/'
    headers = {
        'Authorization': 'JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNjg3OTM3ODMxLCJlbWFpbCI6ImFkbWluQHRlc3QuMTIzIn0.MUypVYFdMMt0AIT28y6hu-cSzQHwRSemVpPiEWTZ1fk',
    }
    
    data = {
        'device': '3797c3e2-ae2d-44ec-b1ff-9beb54884fc9',
        'sn': 'EFACU0010083',
        'card_type':'GCU'
    }

    response = requests.patch(url=url,
    data = data,
    headers=headers)
    print(response.text)
    res_status.append(response.status_code)

    print(repr(res_status))
    print(len(res_status))
# login('admin','admin')
sn_str = '''EFAA52021001
EFAA52021006
EFAA52021021
EFAA52021025
EFAA52021048
EFAA52021058
EFAA52021067
EFAA52021069
EFAA52021072
EFAA52021074
EFAA52021085
EFAA52021094
EFAA52021098
EFAA52021100
EFAA52021109
EFAA52021123'''
#sn_list = []
# print(repr(len(sn_str)))
# sn = ''
# for w in sn_str:
#     if len(sn) == 12:
#         sn_list.append(sn)
#         sn = ''
#     sn += w
# sn_list.append(sn)
# print(repr(sn_list))
# print(len(sn_list))
# request_api(sn_list)
sn_list = sn_str.split('\n')
print(sn_list)
token = login('admin','a$0@T2330')
request_api(sn_list)
