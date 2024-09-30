from django.db import models
from django.utils import timezone
from .supplier import Supplier

class SupplyRequest(models.Model):
    website_name = models.CharField(max_length=100, default='Riot Stor') 
     # Default value COOL BREEZE
    name = models.CharField(max_length=100,default="AS")
    request_date = models.DateTimeField(default=timezone.now)  # Automatically add the current date and time
    category = models.CharField(max_length=100)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, default="pending")
    Supplier= models.ForeignKey(Supplier, on_delete=models.CASCADE,default=1) 

    def __str__(self):
        return self.name  # Customize the display of SupplyRequest instances in the admin

    class Meta:
        verbose_name = "Supply Request"
        verbose_name_plural = "Supply Requests"
