from django.urls import path
from .views import filter,adddata,home,about,contact_view,recipient_list,edit_recipient,delete_recipient



urlpatterns =[
    path("filter/",filter,name="filter"),
    path('adddata/',adddata,name="adddata"),
     path('viewdata/',recipient_list, name='recipient_list'),
    path('edit/<int:pk>/', edit_recipient, name='edit_recipient'),
    path('delete/<int:pk>/',delete_recipient, name='delete_recipient'),
    path('',home,name="home"),
    path("contact/", contact_view, name="contact"),
    # path('adminlogin/',name='admin_login'),
    path('about/',about,name="about"),

]