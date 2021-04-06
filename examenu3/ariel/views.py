from django.shortcuts import render,HttpResponse

# Create your views here.
def inicio1(request):
    return render(request, "index.html")