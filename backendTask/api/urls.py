from django.urls import path
from . import views

urlpatterns = [
    path('', views.getData, name='getData'),
    path('rest/v1/calendar/init/', views.GoogleCalendarInitView, name='credentials'),
    path('rest/v1/calendar/redirect/', views.GoogleCalendarRedirectView, name='redirect'),
]