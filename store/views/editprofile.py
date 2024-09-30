from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from store.models import Category, Product, Order,Customer, Admins

from django.views import View

class EditProfileView(View):
    def get(self, request):
        customer_id = request.session.get('customer')
        sustomers=Customer.objects.filter(id=customer_id)      
        return render(request,'editprofile.html',{ 'ck': sustomers})

    def post(self, request):
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)
        
        customer.name = request.POST.get('name')
        customer.email = request.POST.get('email')
        customer.phone = request.POST.get('phone')
       
        
        
        customer.save()
        
        return redirect('profile') 

        # Redirect to the profile page after saving  
        #         