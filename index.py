import requests
import json

# kodi communication using jesonrpc interface
# retriving the now plying data from kodi.
# the next steps is to send those data to my google calender

#Need to learn -
# google calender api
def what_in_kodi():
    url = "http://192.168.0.2:8080/jsonrpc"

    # Example echo method
    payload = {"jsonrpc": "2.0", "method": "Player.GetItem", "params": { "properties": ["title", "album", "artist", "season", "episode", "duration", "showtitle", "tvshowid", "thumbnail", "file", "fanart", "streamdetails"], "playerid": 1 }, "id": "VideoGetItem"}
    response = requests.post(url, json=payload).json()
    # print(json.dumps(response['result'], indent=4))
    with open('response.json', 'w') as outfile:
        json.dump(response['result'], outfile)
    with open('response.json') as playing_now:
        read_content = json.load(playing_now)
        showname_detail = read_content['item']
        showname = showname_detail['showtitle']
        season = showname_detail['season']
        episode = showname_detail['episode']
        currently_watching = showname
        playing_season = season
        playing_epoisode = episode
        return("Currently Playing {} Season {} Episode {}".format(currently_watching, playing_season, playing_epoisode))
if __name__ == "__main__":
    what_in_kodi()
now_playing = what_in_kodi()
print(now_playing)