from django.urls import path,include
from django.urls import path
from App1.views import *
app_name='App1'
urlpatterns=[
    path('app1_Function/', app1_Function, name='app1_Function'),
]

