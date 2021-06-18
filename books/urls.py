from django.urls import path
from . import views

app_name = 'books'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('book/<int:pk>/', views.BookView.as_view(), name='book'),
    path('author/<int:pk>', views.AuthorView.as_view(), name='author'),
]
