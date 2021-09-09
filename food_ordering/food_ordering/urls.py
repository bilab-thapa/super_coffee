
from django.urls import path, include

urlpatterns = [
    path('foods/', include('foods.urls')),
    path('admins/', include('admins.urls')),
    path('', include('accounts.urls')),
]
