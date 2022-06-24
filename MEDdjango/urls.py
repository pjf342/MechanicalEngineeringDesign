from django.contrib import admin
from django.urls import path
from pages.views import home_view, pvs_view, scw_view, ps_view, register_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),
    path('cylindrical_pressure_vessel_stress/', pvs_view, name='pv'),
    path('strength_and_cold_work/', scw_view, name='scw'),
    path('principal_stresses/', ps_view, name='ps'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
]
