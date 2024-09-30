from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from store.models import Category, Product, Order,Customer, Admins

from django.views import View

class ProfileView(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        sustomers=Customer.objects.filter(id=customer_id)      
        return render(request,'profile.html',{ 'ck': sustomers})