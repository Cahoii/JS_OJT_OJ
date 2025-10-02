from django.urls import path, include

from ..views.oj import AnnouncementAPI

urlpatterns = [
    path("announcement/?$", AnnouncementAPI.as_view(), name="announcement_api"),
]
