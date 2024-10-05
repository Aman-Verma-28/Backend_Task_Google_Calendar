from urllib import response
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render, HttpResponse, redirect
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import pickle
import fickling

@api_view(['GET'])
def getData(request):
    return Response({'data': 'Hello World'})

@api_view(['GET'])
def GoogleCalendarInitView(request):
    scopes = [
        'https://www.googleapis.com/auth/calendar'
    ]
    client_secret = {"web":{"client_id":"199770124160-qaavpob3iv6nll9gj211bq8g7jlpjecg.apps.googleusercontent.com","project_id":"chatbot-2-svlr","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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"}}
    # client_secret = {"installed":{"client_id":"199770124160-0pfn2bsk0k0vskltlmrj3l176kflhsps.apps.googleusercontent.com","project_id":"chatbot-2-svlr","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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"}}
    
    flow = InstalledAppFlow.from_client_config(client_secret, scopes=scopes)
    credentials = flow.run_local_server()
    return response(credentials)


def GoogleCalendarRedirectView(request):
    # Get my credentails

    scopes = [
        'https://www.googleapis.com/auth/calendar'
    ]
    client_secret = {"web":{"client_id":"199770124160-qaavpob3iv6nll9gj211bq8g7jlpjecg.apps.googleusercontent.com","project_id":"chatbot-2-svlr","auth_uri":"https://accounts.google.com/o/oauth2/auth","token_uri":"https://oauth2.googleapis.com/token","auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs","client_secret":"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"}}
    flow = InstalledAppFlow.from_client_config(client_secret, scopes=scopes)
    credentials = flow.run_local_server()
    pickle.dump(credentials, open("token.pkl", "wb"))

    credentials = fickling.load(open("token.pkl", "rb"))

    service = build("calendar", "v3", credentials = credentials)
    
    # Get My calendar

    myCalendar =  service.calendarList().list().execute()

    calendar_id = myCalendar['items'][0]['id']

    # Get My Calendar events
    events = service.events().list(calendarId = calendar_id, timeZone = "Asia/Kolkata").execute()

    # Redirecting it using the event object created 
    
    # return response(events)

    # Redirecting it using the endpoint of google calendar
    return redirect('https://accounts.google.com/o/oauth2/auth?client_id=199770124160-0pfn2bsk0k0vskltlmrj3l176kflhsps.apps.googleusercontent.com&redirect_uri=http://localhost:8000/rest/v1/calendar/redirect&response_type=code&scope=https://www.googleapis.com/auth/calendar&access_type=offline&include_granted_scopes=true&state=state_parameter_passthrough_value&prompt=consent')

