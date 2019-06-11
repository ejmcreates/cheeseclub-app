from django.shortcuts import render, get_object_or_404
from .models import Cheese, CheeseType, Review, Resource
from .forms import CheeseForm, ResourceForm
from django.contrib.auth.decorators import login_required

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

#Cheese resources
def getinfo(request):
    info_list=Resource.objects.all()
    return render(request, 'cheeseapp/resources.html', {'info_list': info_list})

#Add new cheese
@login_required
def newCheese(request):
     form=CheeseForm
     if request.method=='POST':
          form=CheeseForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=CheeseForm()
     else:
          form=CheeseForm()
     return render(request, 'cheeseapp/newcheese.html', {'form': form}) 

#Add new resource
@login_required
def newResource(request):
     form=ResourceForm
     if request.method=='POST':
          form=ResourceForm(request.POST)
          if form.is_valid():
               post=form.save(commit=True)
               post.save()
               form=ResourceForm()
     else:
          form=ResourceForm()
     return render(request, 'cheeseapp/newresource.html', {'form': form}) 

#login and logout
def loginmessage(request):
    return render(request, 'cheeseapp/loginmessage.html')

def logoutmessage(request):
    return render(request, 'cheeseapp/logoutmessage.html')
