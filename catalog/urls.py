from django.urls import path
from .views import catalog_view, books_view

urlpatterns = [
    path('', catalog_view),
    path('books/', books_view, name='books'),
]

