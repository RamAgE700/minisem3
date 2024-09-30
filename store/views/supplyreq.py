# views.py

from django.shortcuts import render
from store.models.supplyreq import SupplyRequest
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib import messages
from django.shortcuts import  get_object_or_404
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.http import HttpResponse



def submit_supply_request(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name:  # Check if 'name' is not empty
            
            quantity = request.POST.get('quantity')
            
            # Save request details to the database
            website_name = "RIOT STORE"  # Default website name
            request_date = timezone.now()  # Current date and time
            SupplyRequest.objects.create(
                website_name=website_name,
                request_date=request_date,
                name=name,
                
                quantity=quantity
            )

            # You can add a success message or redirect here if needed
        else:
            # Handle case where 'name' is empty
            return JsonResponse({"message": "Name field cannot be empty."})

    # After submitting the form, retrieve all supply requests
    supply_requests = SupplyRequest.objects.all()
    
    # Pass the supply requests data to the template for rendering
    return render(request, 'admins/supplyreq.html', {'supply_requests': supply_requests, 'success_message': 'Supply request successfully'})

def supplier_requests(request):
    # Retrieve all supply requests from the database
    supply_requests = SupplyRequest.objects.all()  # Get all requests

    # Pass the supply requests data to the template for rendering
    return render(request, 'admins/supplyreq.html', {'supply_requests': supply_requests})

def delete_supply_request(request, request_id):
    
        # Retrieve the supply request object or return a 404 error if it doesn't exist
        supply_request = get_object_or_404(SupplyRequest, pk=request_id)
        
        # Delete the supply request
        supply_request.delete()
        return redirect('supplier_requests')
    
    

