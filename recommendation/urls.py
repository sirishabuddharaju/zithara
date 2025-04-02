from django.urls import path
from .views import filter,adddata,home,about



urlpatterns =[
    path("filter/",filter,name="filter"),
    path('adddata/',adddata,name="adddata"),
    path('',home,name="home"),
    # path('contact/',name="contact_view"),
    # path('adminlogin/',name='admin_login'),
    path('about/',about,name="about"),

]