from django.shortcuts import render
from main.models import Product, Category, Review

# Create your views here.
def index(request):
    dict_ = {
        'key': 'Students:',
        'color': 'red',
        'list_': ['Adil', 'Torokeldi', 'Nursultan', 'Aiba']
    }
    return render(request, 'index.html', context=dict_)

def product_list_view(request):
    context = {
        'product_list': Product.objects.all(),
        'category_list': Category.objects.all()
    }
    return render(request, 'products.html', context=context)

def product_detail_view(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'detail.html', context={'product_detail': product, 'category_list': Category.objects.all(), 'reviews': Review.objects.filter(product=product)})
def category_product_filter_view(request, category_id):
    context = {
        'product_list': Product.objects.filter(category_id=category_id),
        'category_list': Category.objects.all()
    }
    return render(request,'products.html', context=context)
