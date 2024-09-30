from store.models import Product



def zero_stock_products(request):
    """Context processor to add out-of-stock products to the context."""
    products_with_zero_stock = Product.objects.filter(quantity=0)
    return {'zero_stock_products': products_with_zero_stock}
# from .models import Product

# def zero_stock_products(request):
#     products_with_zero_stock = Product.objects.filter(quantity=0)
#     print("Zero stock products:", products_with_zero_stock)  # Temporary print statement for debugging
#     return {'zero_stock_products': products_with_zero_stock}