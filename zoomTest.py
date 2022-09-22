
import jwt
import requests
import json
from time import time
  
  
# Enter your API key and your API secret
API_KEY = 'lDKqAY5pRsiF5lO6AA_oKA'
API_SEC = 'GQhnVoXAMs0khCRCWMa519CIig9CgWzUi8YE'
  
# create a function to generate a token
# using the pyjwt library
  
  
def generateToken():
    token = jwt.encode(
    
    # Create a payload of the token containing
    # API Key & expiration time
    {'iss': API_KEY, 'exp': time() + 5000},

    # Secret used to generate token signature
    API_SEC,

    # Specify the hashing alg
    algorithm='HS256'
    )
    return(token)
         
  
# create json data for post requests
meetingdetails = {"topic": "ROBB Test",
                  "type": 2,
                  "timezone": "America/New_York",
                  "agenda": "test",
                  "settings": {"host_video": "true",
                               "participant_video": "true",
                               "join_before_host": "true",
                               "mute_upon_entry": "False",
                               "watermark": "false",
                               "audio": "voip",
                               }
                  }
  
# send a request with headers including
# a token and meeting details
  
def createMeeting():
    headers = {'authorization': 'Bearer ' + generateToken(),
               'content-type': 'application/json'}
    r = requests.post(
        f'https://api.zoom.us/v2/users/me/meetings',
        headers=headers, data=json.dumps(meetingdetails))
  
    print("\n creating zoom meeting ... \n")
    print(r.text)
    # converting the output into json and extracting the details
    y = json.loads(r.text)
    join_URL = y["join_url"]
    meetingPassword = y["password"]
    meetingId = y["id"]
  
    print(
        f'\n here is your zoom meeting link {join_URL}, meeting ID {meetingId} and your password: "{meetingPassword}"\n')
  
  
# run the create meeting function
createMeeting()