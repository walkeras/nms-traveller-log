from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='bases'),
    path('<int:base_id>', views.base, name='base'),
]