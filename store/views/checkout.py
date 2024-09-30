from django.shortcuts import redirect
from django.views import View
from django.contrib import messages
from store.models import Order, Customer, Product

class Checkout(View):
    def get(self, request):
        return redirect('cart')
    
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        cart = request.session.get('cart')
        products = Product.getProductById(list(cart.keys()))
        customer = request.session.get('customer')
        print(address, phone, cart, products, customer)

        for product in products:
            quantity = cart[str(product.id)]
            if product.quantity >= quantity:
                # Update the product's stock
                product.quantity -= quantity
                product.save()

                # Create a new order
                newOrder = Order(
                    product=product,
                    customer=Customer(id=customer),
                    quantity=quantity,
                    price=product.price,
                    address=address,
                    phone=phone,
                )
                newOrder.save()
            else:
                # If not enough stock, add an error message and redirect back to the cart
                messages.error(request, f"Not enough stock for {product.name}.")
                return redirect('cart')

        # Clear the cart after successful checkout
        request.session['cart'] = {}
        messages.success(request, "Checkout successful!")
        return redirect('viewBill')