from django.db import models
from store.models import Category, Product
from django.core.files.storage import FileSystemStorage
import random


def addcat(request):
    UserProfile=Category()
    UserProfile.name=request.POST.get('cate')
    suss= UserProfile.save()
    return 1
def editcat(request,ids):
    UserProfile=Category.objects.get(id=ids)
    UserProfile.name=request.POST.get('cate')
    UserProfile.save()
    return 1
def addprodcut(request):
    product=Product()
    product.name=request.POST.get('sname')
   # Category.objects.get(id=post['category'])
    product.category=Category.objects.get(id=request.POST.get('sp'))
    product.description=request.POST.get('sdic')
    product.price=request.POST.get('sprce')
    product.image=request.FILES['prdimg']
    suss= product.save()
    return 1

def eduitprodcut(request, ids):
    product = Product.objects.get(id=ids)
    product.name = request.POST.get('sname')
    product.category = Category.objects.get(id=request.POST.get('sp'))
    product.description = request.POST.get('sdic')
    product.price = request.POST.get('sprce')
    product.image = request.FILES['prdimg']
    product.quantity = request.POST.get('spqty')  # Adding quantity
    product.save()
    return 1