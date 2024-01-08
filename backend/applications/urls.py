from django.urls import path
from . views import ApplicationList

urlpatterns = [
    path('apply/', view=ApplicationList.as_view(), name='apply')
]