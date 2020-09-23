from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import requests
import json
from datetime import datetime, timedelta
# from datetime import date
# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

# reusing the code I wrote to retrive what is now playing on my kodi device, specificly episode data.

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

# current time function, this return the date time as a iso formate, this is neccessary to push the valid formate to google api
def current_Time():
    my_date = datetime.now()
    return my_date.isoformat()
# similar code by this time i am adding 30 minute to my current time. as it's the lenght of the episode i am now playing
def appro_Watchtime():
    approwatchtime = datetime.now() + timedelta(hours=0.5)
    return approwatchtime.isoformat()

# test print approximate watchtime
# print(appro_Watchtime())
# Google api code

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

if __name__ == '__main__':
    googlecalapi()
    what_in_kodi()
    # custom_Function()
