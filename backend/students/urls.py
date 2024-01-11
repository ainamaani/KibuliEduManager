from django.urls import path
from . views import StudentList, StudentDetail

urlpatterns = [
    path('add_student/', StudentList.as_view(), name='add_student'),
    path('/', StudentList.as_view(), name='students'),
    path('delete/<int:pk>/', StudentList.as_view(), name='delete_student'),
    path('update/<int:pk>/', StudentList.as_view(), name='update_student'),
    path('student/<int:pk>', StudentDetail.as_view(), name='student_details')
]