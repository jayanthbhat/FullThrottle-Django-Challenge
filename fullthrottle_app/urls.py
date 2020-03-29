
from django.urls import path
from fullthrottle_app.api import UserListAPIView
from fullthrottle_app.views import command_upload

# url for fullthrottle_app
urlpatterns = [
    path('api/list/',UserListAPIView.as_view(), name="list_api"),
    path('api/throttle-command/',command_upload,name="command"),
]