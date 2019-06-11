from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getcheese/', views.getcheese, name='cheese'),
    path('cheesedetails/<int:id>', views.cheesedetails, name='details'),
    path('getinfo/', views.getinfo, name='resource'),
    path ('newCheese/', views.newCheese, name='newcheese'),
    path ('newResource/', views.newResource, name='newresource'),
    path('loginmessage/', views.loginmessage, name='loginmessage'),
    path('logoutmessage/', views.logoutmessage, name='logoutmessage'),
]