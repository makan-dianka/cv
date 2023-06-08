from django.shortcuts import render
from .. models.cv import CvTheque
from .. models.cv import Job
from django.contrib.auth.models import User

def cvtheque(request):
    user = User.objects.get(username='makan')
    cv = CvTheque.objects.filter(owner=user).last()
    return render(request, 'cvapp/cvtheque.html', {'cv' : cv})