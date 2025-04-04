from django.urls import path
from .views import filter,adddata,home,about,contact_view,recipient_list,edit_recipient,admin_login,recipient_update,admin_logout,recipient_delete,delete_recipient,user_login,register,user_logout



urlpatterns =[
    path("filter/",filter,name="filter"),
    path('adddata/',adddata,name="adddata"),
    path('updatedata/',recipient_update,name="recipient_update"),
    path('deletedata/', recipient_delete, name="recipient_delete"),
    path('viewdata/',recipient_list, name='recipient_list'),
    path('edit/<int:pk>/', edit_recipient, name='edit_recipient'),
    path('delete/<int:pk>/',delete_recipient, name='delete_recipient'),
    path('home/',home,name="home"),
    path("contact/", contact_view, name="contact_view"),
    path('admin-login/', admin_login, name='admin_login'),
    path("", register, name="register"),
    path('login/', user_login, name='user_login'),
    path('about/',about,name="about"),
    path("logout/", user_logout, name="user_logout"),
    path("adminlogout/", admin_logout, name="admin_logout"),

]