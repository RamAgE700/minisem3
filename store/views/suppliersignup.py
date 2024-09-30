from django.shortcuts import render, redirect
from django.views import View
from store.models.supplier import Supplier
from django.contrib.auth.hashers import make_password

class SupplierSignupView(View):
    def get(self, request):
        return render(request, 'suppliersignup.html')
            
    def post(self, request):
        userData = request.POST
        
        # validate
        error = self.validateData(userData)
        if error:
            return render(request, 'suppliersignup.html', {"error": error, "userData": userData})
        else:
            if Supplier.objects.filter(emails=userData['email']).exists():  # Changed 'email' to 'emails'
                error["emailExits_error"] = "Email Already Exists"
                return render(request, 'suppliersignup.html', {"error": error, "userData": userData})
            else:
                new_supplier = Supplier(
                    name=userData['name'],
                    emails=userData['email'],  # Changed 'email' to 'emails'
                    phone=userData['phone'],
                    password=make_password(userData['password']),
                )
                new_supplier.save()
                return redirect('supplierlogin')  # Assuming 'supplierlogin' is the name of the login URL

    # Validate form method
    def validateData(self, userData):
        error = {}
        if not userData['name'] or not userData['email'] or not userData['phone'] or not userData['password'] or not userData['confirm_password']:
            error["field_error"] = "All fields are required"
        elif len(userData['password']) < 8 or len(userData['confirm_password']) < 8:
            error['minPass_error'] = "Password must be at least 8 characters"
        elif len(userData['name']) > 25 or len(userData['name']) < 3:
            error["name_error"] = "Name must be 3-25 characters"
        elif len(userData['phone'])!= 10:
            error["phoneNumber_error"] = "Phone number must be 10 characters"
        elif userData['password']!= userData['confirm_password']:
            error["notMatch_error"] = "Passwords don't match"   

        return error
        return error