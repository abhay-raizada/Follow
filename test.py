import facebook
import requests
import json
def get_fb_token(app_id, app_secret):           
    payload = {'grant_type': 'client_credentials', 'client_id': app_id, 'client_secret': app_secret}
    file = requests.post('https://graph.facebook.com/oauth/access_token?', params = payload)
    print(file.text) #to test what the FB api responded with
    access_dict = json.loads(file.text)
    result = access_dict['access_token']
    #print file.text #to test the TOKEN
    return result
app_id = 116060335750772
app_secret = 'a89ee7c0e3eb03ffe33f99854871a053'
access_token = get_fb_token(app_id, app_secret)
graph = facebook.GraphAPI(access_token) 
print(graph.get_connections('causeSamit', 'feed'))
