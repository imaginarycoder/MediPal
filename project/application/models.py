from django.db import models

# Create your models here.
class Subscribers(models.Model):
    email = models.EmailField(max_length = 264, unique = True)