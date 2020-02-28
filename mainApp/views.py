from django.shortcuts import render

def index(request):
    return render(request, 'mainApp/homePage.html', )
def phonk(request):
    return render(request, 'mainApp/basic.html',)
# Create your views here.
