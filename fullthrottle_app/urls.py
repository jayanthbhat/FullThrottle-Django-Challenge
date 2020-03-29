
from django.urls import path
from fullthrottle_app.api import UserListAPIView
from fullthrottle_app.views import command_upload,home

# url for fullthrottle_app
urlpatterns = [
    path('',home,name="home"),
    path('api/list/',UserListAPIView.as_view(), name="list_api"),
    path('throttle-command/',command_upload,name="command"),
]