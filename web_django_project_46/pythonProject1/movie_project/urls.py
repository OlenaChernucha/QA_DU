from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
]
