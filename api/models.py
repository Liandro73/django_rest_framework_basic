from django.db import models
from django.db.models import CASCADE

# Create your models here.
class User(models.Model):
    age = models.IntegerField(null=False)
    name = models.CharField(max_length=100, null=False)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

class Address(models.Model):
    user = models.ForeignKey(User, related_name='addresses', null=False, on_delete=CASCADE)
    address_line_one = models.CharField(max_length=100, null=False)
    address_line_two = models.CharField(max_length=50, null=True)
    number = models.IntegerField(null=False)
    postal_code = models.CharField(max_length=20, null=False)
    city = models.CharField(max_length=50, null=False)
    state = models.CharField(max_length=50, null=False)
    country = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.address_line_one