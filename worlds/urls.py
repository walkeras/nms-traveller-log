from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='worlds'),
    path('<int:world_id>', views.world, name='world'),
    path('search', views.search, name="worlds_search"),
]