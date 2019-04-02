from django.urls import path

from tinyfood.views import json_index


urlpatterns = [
    path('json_index', json_index, name='json_index'),
]