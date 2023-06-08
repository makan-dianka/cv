from django.shortcuts import render

def cvtheque(request):
    return render(request, 'cvapp/cvtheque.html')