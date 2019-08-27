import requests
from twilio.rest import Client

#Twilio ID
client=Client('AC1cf3e49ae59552167dbcf13a5ef4fc3c','5058d6f683d9d013ef7ddb3790bec6bb')

#route Twitch expose data
endpoint='https://api.twitch.tv/helix/streams?'

#Authenticate our API key
headers= {'Client-ID':'i0h7yfam8pjzhxy1f9x53ytpcl3xl3'}

#Twitcher we want to follow
params={'user_login':'drlupo'}

#make the request 
response=requests.get(endpoint,params=params,headers=headers)

#returns data format as JSON
json_response=response.json()
streams=json_response.get('data',[])

#The test if stream is live or offline
is_active= lambda stream:stream.get('type')=='live'

#filters the array of streams and only keeps active streams
streams_active=filter(is_active,streams)

#returns if any stream is active
activeStreams=any(streams_active)

#sends text message
if activeStreams:
    client.messages.create(body='DrLupo is Live!',from_='18482259187',to='3475220581')
    
