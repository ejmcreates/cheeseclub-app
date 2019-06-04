from django.contrib import admin
from .models import CheeseType, Cheese, Resource, Review

# Register your models here.
admin.site.register(CheeseType)
admin.site.register(Cheese)
admin.site.register(Resource)
admin.site.register(Review)
