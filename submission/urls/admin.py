from django.urls import path, include

from ..views.admin import SubmissionRejudgeAPI

urlpatterns = [
    path("submission/rejudge?$", SubmissionRejudgeAPI.as_view(), name="submission_rejudge_api"),
]
