import urllib
import json
import requests
CLIENT_ID = 'j3abopdoj1fi9hshxtli9jlnkyruof'
CLIENT_SECRET='ybud1f2qvv2u89s8ue8wpsdb7f88pc'

def make_request(URL):
   header    = {"Client-ID": CLIENT_ID, "Authorization": f"Bearer {get_access_token()}" }
   req  = urllib.request.Request(URL, headers=header)
   recv = urllib.request.urlopen(req)
   return json.loads(recv.read().decode("utf-8"))
def get_access_token(): 
    x = requests.post(f"https://id.twitch.tv/oauth2/token?client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials")
    print(json.loads(x.text)["access_token"])
    return json.loads(x.text)["access_token"]

topgames = make_request("https://api.twitch.tv/helix/search/channels?query=benjyfishy")
print(topgames['data'][0])
    