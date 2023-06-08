from django.urls import path
from . views import cvtheque

app_name = "cvapp"
urlpatterns = [
    path('', cvtheque.cvtheque, name='cvtheque')
]