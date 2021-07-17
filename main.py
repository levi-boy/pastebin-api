import os
import json

import requests


def new_paste(api_dev_key: str, data: json):
    # set paste privacy status
    api_paste_private = 2
    privacy_status = data['privacy_status']
    if privacy_status == 'public':
        api_paste_private = 0
    elif privacy_status == 'unlisted':
        api_paste_private = 1
    
    data = {
        'api_option': 'paste',
        'api_dev_key': api_dev_key,
        'api_paste_code': data['text'],
        'api_paste_private': api_paste_private,
        'api_paste_expire_date': data['paste_expire_date'],
        'api_paste_format': 'php',
        'api_user_key': '',
    }

    url = 'https://pastebin.com/api/api_post.php'

    r = requests.post(url, data=data)
    return r.text


data = {'text': 'holop let me get a story',
        'paste_expire_date': '1Y',
        'privacy_status': 'public'}
paste_response = new_paste(api_dev_key=os.getenv('pastebin_api_key'), data=data)

print(paste_response)
