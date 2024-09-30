from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from store.models import Category, Product, Order,Customer, Admins
from .dbset import addcat,editcat,addprodcut,eduitprodcut
from django.shortcuts import render
from store.models import Product, Order
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from store.models.supplier import Supplier
from store.models.supplyreq import SupplyRequest
from store.models.SupplierProduct import SupplierProduct
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.units import mm
from reportlab.lib import colors
from datetime import timedelta
from django.contrib import messages
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from store.models.category import Category  # Import the Category model
from django.http import HttpResponseBadRequest

def viewprdlist(request):
       
        supplier_products = SupplierProduct.objects.all()
        context = {
            'in_stock_': supplier_products,
            
        }
        return render(request, 'supprolist.html ', context)