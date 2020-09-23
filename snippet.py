# this part o
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
        showname = showname_detail['streamdetails']['video']
        duration = dict(showname[0].values())
        actual_duration = duration[2]
