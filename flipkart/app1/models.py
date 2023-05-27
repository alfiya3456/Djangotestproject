from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.DecimalField(max_digits=4,decimal_places=2)
    description = models.CharField(max_length=500)


#ORM Queries --->query set providing django
"""
Tablename.objects.all()    #all values display
Tablename.objects.all().values()  #particular value display
Tablename.objects.get(id=1)  # particular id/object display
delete()  # delete values
save()  # save values


"""