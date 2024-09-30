from django.db import models
from .supplier import Supplier

class SupplierProduct(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'Pending Approval'),
        ('Approved', 'Approved'),
    )
    
    product_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    supply_charge = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_items = models.PositiveIntegerField()
    date_of_supply = models.DateField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    description = models.TextField()
    image = models.ImageField(upload_to='supplier_images/', default='default_image.jpg')
    Supplier= models.ForeignKey(Supplier, on_delete=models.CASCADE)
   
    
    def __str__(self):
        return self.product_name
