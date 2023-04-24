from django.urls import path
from . import views 

urlpatterns = [
    path("", views.index),
    path("register", views.register),
    path("events", views.events),
    path("logout", views.logout),
    path("login", views.login),
    path("events/add", views.addevent),
    path("createtrip", views.createtrip),
    path("destination/<tripID>", views.tripdetails),
    path("JoinTrip/<tripID>", views.JoinTrip),
    path("cancel/<tripID>", views.cancel),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('index/', views.index, name='index')
]
 