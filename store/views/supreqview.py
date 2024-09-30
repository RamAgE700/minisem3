# store/views/supreqview.py
from django.shortcuts import render , redirect
from django.http import JsonResponse
from store.models.supplyreq import SupplyRequest  # Import the SupplyRequest model

def view_messages(request):
    # Retrieve all supply requests from the database
    supply_requests = SupplyRequest.objects.all()

    # Pass the supply requests data to the template for rendering
    return render(request, 'supreqview.html', {'supply_requests': supply_requests})

def process_request(request, request_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        if action in ['accept', 'reject']:
            # Logic to accept or reject the request
            request = SupplyRequest.objects.get(id=request_id)
            request.status = action.capitalize()  # Assuming 'status' is a field in the SupplyRequest model
            request.save()
            return JsonResponse({'status': 'success'})  # Return success response as JSON
    return JsonResponse({'status': 'error'}, status=400)  # Return error response as JSON

def complete_request(request, request_id):
  supply_request = SupplyRequest.objects.get(pk=request_id)
  supply_request.status = 'conformed'
  supply_request.save()
  return redirect('view_supply_requests')

def reject_request(request, request_id):
  supply_request = SupplyRequest.objects.get(pk=request_id)
  supply_request.status = 'rejected'
  supply_request.save()
  return redirect('view_supply_requests')

def delete_request(request, request_id):
    supply_request = SupplyRequest.objects.get(pk=request_id)
    supply_request.delete()
    return redirect('view_supply_requests')

def delete_rejected_requests(request):
    # Delete all supply requests with status 'rejected'
    SupplyRequest.objects.filter(status='rejected').delete()
    return redirect('view_supply_requests')