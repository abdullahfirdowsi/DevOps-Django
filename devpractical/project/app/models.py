from django.db import models

# Create your models here.
class app_db(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

 