from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

from tinyfood.models import (
    FarmRegion, FarmStyle, FarmBusiness, Farmer, ProductType, Product, ProductOrder)


def json_index(request):
    farmers = Farmer.objects.filter(active=True)
    products = Product.objects.filter(available=True)

    data = {
        'products': serialize('json', products),
        'farmers': serialize('json', farmers),
    }
    return JsonResponse(data)
