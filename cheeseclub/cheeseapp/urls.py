from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('gettypes/', views.gettypes, name='types'),
    path('getcheese/', views.getcheese, name='cheese'),
    path('cheesedetails/<int:id>', views.cheesedetails, name='details')
]