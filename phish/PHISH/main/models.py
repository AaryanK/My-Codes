from django.db import models
from django.db.models.query_utils import select_related_descend

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    valid = models.CharField(max_length=100,choices=(("VALID","VALID"),("INVALID","INVALID")),null=True)



    def __str__(self):
        return self.username