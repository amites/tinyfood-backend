from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

from tinyfood.models import (
    FarmRegion, FarmStyle, FarmBusiness, Farmer, ProductType, Product, ProductOrder)


def json_index(request): 
    farmers_data = []
    for farmer in Farmer.objects.filter(active=True):
        farmers_data.append({
            'name': farmer.user.get_full_name(),
            'business': farmer.farm.name,
            'region': getattr(getattr(farmer.farm, 'region'), 'name'),
            'farming_style': farmer.farm.farming_style.name,
            'address': farmer.farm.address_str,
            'email': farmer.user.email,
            'phone': farmer.user.userprofile.phone,
            'insta': farmer.user.userprofile.instagram,
            'liason': farmer.user.userprofile.liason,
            'seasonal_orders_avail': '',
        })
    
    products = Product.objects.filter(available=True)

    data = {
        'products': serialize('json', products),
        'farmers': farmers_data,
    }

    return JsonResponse(data)
