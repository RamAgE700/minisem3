from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from store.models import Category, Product, Order,Customer, Admins

from django.views import View
from django.contrib.auth.hashers import check_password, make_password

class ChangePasswordView(View):
    def get(self, request):
        # Render the password change form
        return render(request, 'change_password.html')

    def post(self, request):
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        
        customer_id = request.session.get('customer')
        customer = Customer.objects.get(id=customer_id)
        
        if not check_password(old_password, customer.password):
            return render(request, 'change_password.html', {'error': 'Incorrect old password'})
        
        if new_password != confirm_password:
            return render(request, 'change_password.html', {'error': 'Passwords do not match'})
        
        customer.password = make_password(new_password)
        customer.save()
        
        return redirect('profile')  # Redirect to the profile page