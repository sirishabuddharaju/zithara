from django.urls import path
from .views import filter


urlpatterns =[
    path("",filter,name="filter"),
]