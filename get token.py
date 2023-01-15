import requests, os

secret = os.environ['TwitchApiSecret']
id = "s7dwe9ds450dsvisqgwue75xl509ps"
ses = requests.Session()
hrs = {
'Content-Type':'application/json',
}
body = {
'client_id':id,
'client_secret':secret,
'grant_type':'client_credentials'
}
Endpoint = "https://id.twitch.tv/oauth2/token"


APICall = ses.post(Endpoint,json=body,headers=hrs)       
print(APICall.json())



