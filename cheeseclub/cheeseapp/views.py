from django.shortcuts import render, get_object_or_404
from .models import Cheese, CheeseType, Review, Resource

# Create your views here.
def index(request):
    return render(request, 'cheeseapp/index.html')

# Cheese types view
def gettypes(request):
    type_list=CheeseType.objects.all()
    return render(request, 'cheeseapp/types.html', {'type_list': type_list})

#Cheese view
def getcheese(request):
    cheese_list=Cheese.objects.all()
    return render(request, 'cheeseapp/cheese.html', {'cheese_list': cheese_list})

#Cheese detail views
def cheesedetails(request, id):
    detail_list=get_object_or_404(Cheese, pk=id)
    return render(request, 'cheeseapp/details.html', {'detail_list': detail_list})


