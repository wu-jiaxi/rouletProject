from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

# Create your models here.
class Ticket(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    status = models.CharField(max_length=50, default='new')
    created_at = models.DateTimeField(auto_now_add=True)