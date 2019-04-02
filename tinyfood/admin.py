from django.contrib import admin

from tinyfood.models import (
    FarmRegion, FarmStyle, FarmBusiness, Farmer, ProductType, Product, ProductOrder)


@admin.register(FarmRegion)
class FarmRegionAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmStyle)
class FarmStyleAdmin(admin.ModelAdmin):
    pass


@admin.register(FarmBusiness)
class FarmBusinessAdmin(admin.ModelAdmin):
    pass


@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductOrder)
class OrderAdmin(admin.ModelAdmin):
    pass
