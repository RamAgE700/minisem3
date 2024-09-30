from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.hashers import make_password
from store.models import Customer

class ForgetPasswordView(View):
    def get(self, request):
        return render(request, 'forget_password.html')

    def post(self, request):
        email = request.POST.get('email')
        new_password = request.POST.get('new_password')
        customer = Customer.objects.filter(email=email).first()
        if customer:
            customer.password = make_password(new_password)
            customer.save()
            return redirect('login')
        else:
            return render(request, 'forget_password.html', {'error': 'User not found'})