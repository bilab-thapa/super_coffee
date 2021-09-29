
from django.urls import path, include

urlpatterns = [
    path('admins/', include('admins.urls')),
    path('products/', include('products.urls')),
    path('', include('accounts.urls')),

]

