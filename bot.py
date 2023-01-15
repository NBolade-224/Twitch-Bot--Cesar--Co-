import requests, time

access_token = "{AccessToken}"
ses = requests.Session()
hrs = {
'Client-Id':"{clientID}",
'Authorization':'Bearer {}'.format(access_token)
}
Endpoint = "https://api.twitch.tv/helix/chat/chatters?broadcaster_id={IDNumber}&moderator_id={IDNumber}"

ListOfUsersAlreadyIn = set()

while True:
    try:
        APICall = ses.get(Endpoint,headers=hrs)       
        userlist = APICall.json()["data"]
    except:
        time.sleep(60)
        continue

    for users in userlist:
        if users not in ListOfUsersAlreadyIn:
            print(users['user_name'])
            ListOfUsersAlreadyIn.add(users['user_name'])
        else:
            continue
    
    time.sleep(15)
