from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('ama/', admin.site.urls),
    path('', include('cvapp.urls')),
]
