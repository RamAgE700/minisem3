from django.shortcuts import render
from store.models import Product

def view_bill(request, product_id):
    try:
        # Attempt to retrieve the product with the given ID
        product = Product.objects.get(pk=product_id)
        
        # Calculate the total price for the product (price * quantity + supply charge)
        total_price = (product.price * product.number_of_items) + product.supply_charge
        
        # Render the viewsupplybill template with the product and total price
        return render(request, 'viewsupplybill.html', {'product': product, 'total_price': total_price})
    except Product.DoesNotExist:
        # If the product does not exist, redirect to the viewsupplybill page
        return render(request, 'viewsupplybill.html')
