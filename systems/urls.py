from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='systems'),
    path('<int:system_id>', views.system, name='system'),
    path('search', views.search, name="systems_search"),
]