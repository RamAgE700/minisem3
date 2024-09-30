from django.db import models
from django.contrib.auth.hashers import make_password

class Supplier(models.Model):
    
    name = models.CharField(max_length=50)
    emails = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15, default='0000000000') 
    
    password = models.CharField(max_length=255, default=make_password('defaultpassword'))

    def __str__(self):
        return self.name
    

    @staticmethod
    def email_exists(userEmail):
        try:
            supplier = Supplier.objects.get(emails=userEmail)
            return supplier
        except Supplier.DoesNotExist:
            return False
            