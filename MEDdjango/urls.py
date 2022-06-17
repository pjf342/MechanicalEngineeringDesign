from django.contrib import admin
from django.urls import path
from pages.views import home_view, pvs_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('pressure_vessel_stress/', pvs_view, name='pv'),
]
