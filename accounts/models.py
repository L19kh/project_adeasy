from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.email
   
class Ad(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ads')
    ad_title = models.CharField(max_length=100)
    ad_description = models.TextField()
    publication_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.ad_title