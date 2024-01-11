from . views import BookList,BookDetail
from django.urls import path

urlpatterns =[
    path('add_book/', BookList.as_view(), name='add_book'),
    path('/', BookList.as_view(), name='books'),
    path('delete/<int:pk>/', BookList.as_view(), name='delete_book'),
    path('update/<int:pk>/', BookList.as_view(), name='update_book'),
    path('book/<int:pk>', BookDetail.as_view(), name='book_details')
]