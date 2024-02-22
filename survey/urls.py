from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views as survey_views 


router = DefaultRouter()
urlpatterns = [
    path("list/" , survey_views.SurveyListView.as_view())
    # path("create/" , survey_views.)
]
