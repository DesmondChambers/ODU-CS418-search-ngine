from django.db import models

# Create your models here.

class User (models.Model):
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    email_address = models.EmailField(null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)
# ...

    def  __str__(self) -> str:
        return self.first_name + ' ' + self.last_name