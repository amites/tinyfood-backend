from django.http import JsonResponse
from django.shortcuts import render

from tinyfood.models import (
    FarmRegion, FarmStyle, FarmBusiness, Farmer, ProductType, Product, ProductOrder)


def all_view(request):
    data = {

    }
    return JsonResponse(data)
