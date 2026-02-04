from django.urls import path

from .views import ItemListView, ItemDetailView , ProductListView , ProductDetailView


urlpatterns = [
    path('books/', ItemListView.as_view()),
    path('books/<int:pk>', ItemDetailView.as_view()),
    path('products/', ProductListView.as_view()),
    path('products/<int:pk>', ProductDetailView.as_view()),
]

