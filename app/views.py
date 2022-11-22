from django.shortcuts import render

# Create your views here.
def gouse(request):
    return render(request,'gouse.html')