from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views import View
from django.contrib.auth.hashers import check_password
from store.models.supplier import Supplier
from django.core.exceptions import ObjectDoesNotExist

class SupplierLoginView(View):
    return_url = None

    def get(self, request):
        SupplierLoginView.return_url = request.GET.get('return_url')
        return render(request, 'supplierlogin.html')

    def post(self, request):
        userData = request.POST
        try:
            supplier = Supplier.objects.get(emails=userData["email"])
            if check_password(userData["password"], supplier.password):
                request.session["supplier_id"] = supplier.id
                if SupplierLoginView.return_url:
                    return HttpResponseRedirect(SupplierLoginView.return_url)
                else:
                    SupplierLoginView.return_url = None
                    return redirect('su_dashboard')
            else:
                return render(request, 'supplierlogin.html', {"error": "Email or password doesn't match"})
        except ObjectDoesNotExist:
            return render(request, 'supplierlogin.html', {"error": "Email or password doesn't match"})
            return render(request, 'supplierlogin.html', {"userData": userData, "error": "Email or password doesn't match"})

def logouts(request):
	request.session.clear()
	return redirect('supplierlogin')
