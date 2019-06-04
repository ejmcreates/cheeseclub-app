from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class CheeseType(models.Model):
    typename=models.CharField(max_length=50)
    typedescription=models.CharField(max_length=255)

    def __str__(self):
        return self.typename

    class Meta:
        db_table='cheesetype'
        verbose_name_plural='cheesetypes'

class Cheese(models.Model):
    cheesename=models.CharField(max_length=255)
    cheesetype=models.ForeignKey(CheeseType, on_delete=models.DO_NOTHING)
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    cheeseentrydate=models.DateField() 
    cheesedesc=models.TextField()
    cheeseprice=models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.cheesename

    class Meta:
        db_table='cheese'
        verbose_name_plural='cheeses'

class Review(models.Model):
    reviewtitle=models.CharField(max_length=255)
    user=models.ManyToManyField(User)
    reviewdate=models.DateField()
    reviewrating=models.SmallIntegerField()
    reviewdesc=models.TextField()
    cheese=models.ForeignKey(Cheese, on_delete=models.DO_NOTHING)   

    def __str__(self):
        return self.reviewtitle

    class Meta:
        db_table='review'
        verbose_name_plural='reviews'

class Resource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=255) 
    url=models.URLField(null=True, blank=True)
    dateentered=models.DateField()
    userid=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    description=models.TextField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='resource'
        verbose_name_plural='resources'

