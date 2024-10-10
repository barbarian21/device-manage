import requests
import json

def get_info(url,token):
    
    headers = {
        'Authorization': 'JWT ' + token,
    }
    response = requests.get(url=url,headers=headers)
    if response.status_code == 200:
        j_rep = json.loads(response.text)
        return j_rep
    else:
        return []

def get_info_page(url,token):

    ret_list = []
    offset = 0
    first_url = url + '?offset= %s' % str(offset)
    j_rep = get_info(first_url,token)
    if j_rep:
        count = j_rep['count']
        ret_list += j_rep['results']
    else:
        return ret_list

    while offset < count:
        offset += 10
        offset_url = url + '?offset= %s' % str(offset)
        j_rep = get_info(offset_url,token)
        if j_rep:
            ret_list += j_rep['results']

    return ret_list