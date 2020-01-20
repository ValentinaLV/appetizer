from django.shortcuts import render

from .models import CateringProduct, CateringCategory


def catering_products_list(request):
    products = CateringProduct.objects.all().filter(available=True)
    categories = CateringCategory.objects.all()

    return render(request, 'catering.html', {
        'products': products,
        'categories': categories,
    })


def catering_product_details(request, slug):
    product = CateringProduct.objects.get(slug=slug)
    return render(request, 'catering_details.html', {
        'product': product
    })
