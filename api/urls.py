from django.urls import path

from .views import ItemListView, ItemDetailView


urlpatterns = [
    path('books/', ItemListView.as_view()),
    path('books/<int:pk>', ItemDetailView.as_view()),
]
