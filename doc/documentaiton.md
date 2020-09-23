Function that return the kodi now paying data with additional information 
```python
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
        duration_list = showname_detail['streamdetails']['video']
        list_duration = list(duration_list[0].values())
        duration = list_duration[2]
        # return showname, season, episode
        # here i am retuning the now playig data as a scring with custom formating
        return("You Watched {} Season {} Episode {} Duration {}".format(showname, season, episode, duration))
```
funtion that pus the data to google calender api and write the event for me
```python
def googlecalapi():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    # now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    # replacing some dictonary data wtih my function returned data
    ev = {
        'summary': 'You Watched',
        # 'location': '',
        # 'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '',
            'timeZone': 'Asia/Dhaka',
        },
        'end': {
            'dateTime': '',
            'timeZone': 'Asia/Dhaka',
        },
    }

    # custom dictonary value

    ev['summary'] = what_in_kodi()
    ev['start']['dateTime'] = current_Time()
    ev['end']['dateTime'] = appro_Watchtime()

    # ev = e + what_in_kodi()

    # Pring the event value
    # print(ev)
    # pushing the data to google calender my primary calender
    service.events().insert(calendarId='primary', body=ev).execute()

```

function that successfully retrive the time duration of the playing media 
```python
def time():
    with open('response.json') as playing_now:
        read_content = json.load(playing_now)
        showname_detail = read_content['item']
        duration_list = showname_detail['streamdetails']['video']
        list_duration = list(duration_list[0].values())
        duration = list_duration[2]
        return duration

```