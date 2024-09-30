from django.shortcuts import render
from ..models import Product

def search_view(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.none()
    return render(request, 'search_results.html', {'products': products, 'query': query})