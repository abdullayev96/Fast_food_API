from django.urls import path
from .views import CategoryProductAPI



urlpatterns = [
    path('cat/', CategoryProductAPI.as_view(), name='category-products'),

]