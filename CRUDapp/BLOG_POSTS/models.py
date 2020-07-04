from django.db import models

# Create your models here.
class CRUD(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.CharField(max_length=200)

