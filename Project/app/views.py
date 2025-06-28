from django.shortcuts import render 
from django.http import HttpResponse
from .models import CarsVariety



# Create your views here.


def home(request):
  return render(request, 'app.html')



def all_Car(request):
  car = CarsVariety.objects.all()
  return render(request, 'app.html', {'cars': car})