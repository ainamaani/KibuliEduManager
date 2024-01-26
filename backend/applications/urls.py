from django.urls import path
from . import views
from . views import ApplicationList, ApplicationDetail

urlpatterns = [
    path('apply/', ApplicationList.as_view(), name='apply'),
    path('', ApplicationList.as_view(), name='applications'),
    path('delete/<int:pk>/', ApplicationList.as_view(), name='delete_application'),
    path('update/<int:pk>/', ApplicationList.as_view(), name='update_application'),
    path('application/<int:pk>', ApplicationDetail.as_view(), name='application_details'),
    path('reject/<int:pk>/',views.reject_application, name='reject_application')
]