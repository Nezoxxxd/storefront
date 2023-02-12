from django.urls import path
from . import views
 # . means that we import smth from currnet folder

#UrlConf
urlpatterns = [
    path('hello/', views.say_hello)   
    # we don't use () with function <say_hello> because we transfer link on this function (we don't call this it)
 ]