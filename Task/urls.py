from django.urls import path
from . import views

urlpatterns = [
    # path('categories/', views.CategoryListCreateView.as_view(), name='category-list'),
    path('categories/', views.CategoryListView.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyView.as_view(), name='category-detail'),
    path('books/', views.BookListCreateView.as_view(), name='book-list'),
    path('books/<int:pk>/', views.BookRetrieveUpdateDestroyView.as_view(), name='book-detail'),
]