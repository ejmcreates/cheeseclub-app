from django.shortcuts import render
from .models import Cheese, CheeseType, Review, Resource

# Create your views here.
def index(request):
    return render(request, 'cheeseapp/index.html')

# Cheese types view
def gettypes(request):
    type_list=CheeseType.objects.all()
    return render(request, 'cheeseapp/types.html', {'type_list': type_list})

