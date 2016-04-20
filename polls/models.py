from django.db import models

# Create your models here.
class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)

class Ticket(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  number = models.IntegerField(default=0)
