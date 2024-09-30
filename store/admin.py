from django.contrib import admin
from .models import Product
from .models import Category
from .models import Customer
from .models import Order
from .models import supplier
from .models import SupplierProduct
from .models import supplyreq
from .models.GameOptimizer import GameOptimization

class AdminProduct(admin.ModelAdmin):
	list_display = ['id', 'name','price','category', 'date' ,]


class AdminCategory(admin.ModelAdmin):
	list_display = ['name']



admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(supplier.Supplier)
admin.site.register(SupplierProduct.SupplierProduct)
admin.site.register(supplyreq.SupplyRequest)
admin.site.register(GameOptimization)

