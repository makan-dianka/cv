from django.shortcuts import render
from .. models.cv import CvTheque
from django.contrib.auth.models import User
import os

def cvtheque(request):
    user = User.objects.get(username=os.getenv('username'))
    cv = CvTheque.objects.filter(owner=user).last()
    return render(request, 'cvapp/cvtheque.html', {'cv' : cv})