from django.urls import path
from App2.views import *
app_name='App2'
urlpatterns=[
    path('app2_Function/',app2_Function,name='app2_Function'),

]