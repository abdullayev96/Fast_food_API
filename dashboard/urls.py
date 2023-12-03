from django.urls import path
from .views import CategoryView


urlpatterns = [

    path('categories/list', CategoryView.as_view(), name="category-list"),
    path('categories/create', CategoryView.as_view(), name="category-create"),
    path('categories/<int:pk>/retrieve', CategoryView.as_view(), name='category-retrieve'),
    path('categories/<int:pk>/update', CategoryView.as_view(), name='category-update'),
    path('categories/<int:pk>/destroy', CategoryView.as_view(), name='category-destroy'),

]
