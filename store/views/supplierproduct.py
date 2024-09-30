# views/supplierproduct.py
from django.shortcuts import render, redirect
from django.views import View
from store.models.SupplierProduct import SupplierProduct 
from store.models.supplier import Supplier # Import the SupplierProduct model

class SupplierDashView(View):
    def get(self, request):
        # Fetch all products added by the supplier
        supplier_products = SupplierProduct.objects.all()
        if not supplier_products:
            return render(request, 'supplierdash.html', {'error': 'No products found.'})
        # Calculate the total price including supply charge for each product
        total_price = sum(product.price + product.supply_charge for product in supplier_products)
        return render(request, 'supplierdash.html', {'supplier_products': supplier_products, 'total_price': total_price})

    def post(self, request):
        # Check if the send button is clicked
        if 'send_button' in request.POST:
            # Fetch all products added by the supplier
            supplier_products = SupplierProduct.objects.all()
            # Calculate the total price including supply charge for each product
            total_price = sum(product.price + product.supply_charge for product in supplier_products)
            # Delete all products added by the supplier
            SupplierProduct.objects.all().delete()
            return render(request, 'supplierdash.html', {'supplier_products': supplier_products, 'total_price': total_price})
        
        # Handle form submission to add a new product
        product_name = request.POST.get('product_name')
        price = float(request.POST.get('price'))  # Convert price to float
        supply_charge = float(request.POST.get('supply_charge'))  # Convert supply charge to float
        number_of_items = int(request.POST.get('number_of_items'))  # Convert number of items to int
        date_of_supply = request.POST.get('date_of_supply')
          # Retrieve color from form
        description = request.POST.get('description')  # Retrieve description from form
        # Handle image upload
        image = request.FILES.get('image')
        current_supplier = Supplier.objects.get(id=request.session.get('supplier_id'))
        # Create a new SupplierProduct object
        new_product = SupplierProduct(
            product_name=product_name,
            price=price,
            supply_charge=supply_charge,
            number_of_items=number_of_items,
            date_of_supply=date_of_supply,
            status='pending',  # Assuming the status is initially set to pending
            description=description,  # Set the description field
            image=image,
            Supplier=current_supplier
              # Set the image field
        )
        new_product.save()

        # Redirect back to the supplier dashboard
        return redirect('supplier_dashboard')

