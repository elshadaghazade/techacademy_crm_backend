from django.urls import path

from .views import *


urlpatterns = [
    path('change_status/', change_status, name='change_status'),
    path('update_date/', update_date, name='update_date'),
    path('get_leads/', get_leads, name='get_leads')
]
