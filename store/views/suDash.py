from django.shortcuts import render, redirect
from django.views import View

from store.models import Category, Product, Order,Customer, Admins
from .dbset import addcat,editcat,addprodcut,eduitprodcut
from django.shortcuts import render
from store.models.SupplierProduct import SupplierProduct
from store.models.supplyreq import SupplyRequest
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.db.models import Sum
from reportlab.lib.styles import getSampleStyleSheet
from store.models.category import Category  # Import the Category model
from django.http import HttpResponseBadRequest

def suDash(request):
    
        
        # Stock management details logic
        total_products = SupplierProduct.objects.count()
        total_requests = SupplyRequest.objects.count()
        total_approved_requests = SupplyRequest.objects.filter(status='Supply soon').count()
        total_pending_requests = SupplyRequest.objects.filter(status='Pending').count()
        
        # Total profit calculation
        total_profit = SupplierProduct.objects.aggregate(total_profit=Sum('price'))['total_profit'] or 0
        print("Total approved requests:", total_approved_requests)
        print("Total pending requests:", total_pending_requests)
        # Get product names and stock counts
        products_stock = SupplierProduct.objects.values('product_name', 'number_of_items')

        context = {
            'total_products': total_products,
            'total_requests': total_requests,
            'total_approved_requests': total_approved_requests,
            'total_pending_requests': total_pending_requests,
            'total_profit': total_profit,
            'products_stock': products_stock,
        }
       
        return render(request, 'suDashboard.html', context)
    