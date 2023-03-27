from django.shortcuts import render

# Create your views here.

def booststrap_cdn(request):
    return render(request,'booststrap_cdn.html')
