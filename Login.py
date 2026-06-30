import json
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def login(url, username, password):
    base_url = 'https://{APICurl}/api/'.format(APICurl=url)

    # create credentials structure
    name_pwd = {'aaaUser': {'attributes': {'name': username,'pwd': password}}}
    json_credentials = json.dumps(name_pwd)

    # log in to API
    login_url = base_url + 'aaaLogin.json'
    post_response = requests.post(login_url, data=json_credentials, verify=False)
    print(post_response)

    # get token from login reponse structure
    auth = json.loads(post_response.text)
    login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
    auth_token = login_attributes['token']

    # create cookie array from token
    cookies = {}
    cookies['APIC-Cookie'] = auth_token
    return cookies

if __name__ == '__main__':
    url = '10.10.20.14'
    username = 'admin'
    password = 'Pass_Master'
    print(login(url, username, password))