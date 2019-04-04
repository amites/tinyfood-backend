from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render

from tinyfood.models import (
    FarmRegion, FarmStyle, FarmBusiness, Farmer, ProductType, Product, ProductOrder, UserProfile)


def json_index(request): 
    farmers_data = []
    for farmer in Farmer.objects.filter(active=True):
        if not getattr(farmer.user, 'userprofile', False):
            farmer.user.userprofile = UserProfile()
            farmer.user.userprofile.save()
        farmers_data.append({
            'name': farmer.user.get_full_name(),
            'business': farmer.farm.name,
            'region': getattr(getattr(farmer.farm, 'region'), 'name', ''),
            'farming_style': getattr(getattr(farmer.farm, 'farming_style'), 'name', ''),
            'address': farmer.farm.address_str,
            'email': farmer.user.email,
            'phone': farmer.user.userprofile.phone,
            'insta': farmer.user.userprofile.instagram,
            'liason': getattr(farmer.user.userprofile, 'liason', ''),
            'seasonal_orders_avail': '',
        })
    
    products_data = []
    for product in Product.objects.filter(available=True):
        products_data.append({
            'id': product.id,
            'picture': product.picture.url,
            'sale': product.sale,
            'organic': product.organic,
            'producer': product.producer.name,
            'type': product.type,
            'available': product.available,
        })

    data = {
        'products': products_data,
        'farmers': farmers_data,
    }

    return JsonResponse(data)
