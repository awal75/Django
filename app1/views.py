from django.shortcuts import render

# Create your views here.

def app_1(request):

    return render(request,'app1/app1.html')