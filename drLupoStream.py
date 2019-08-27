import requests
from twilio.rest import Client

#Twilio ID
client=Client('#Twilio_Account_SID','#Twilio_AUTH_TOKEN')

#route Twitch expose data
endpoint='https://api.twitch.tv/helix/streams?'

#Authenticate our API key
#https://dev.twitch.tv/console/apps
headers= {'Client-ID':'#Your_Twitch_Clinet_ID'}

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
    client.messages.create(body='DrLupo is Live!',from_='#Twilio_Temp_Phone_Number',to='#My_Phone_Number')
    
