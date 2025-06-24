from django.shortcuts import render 
from django.http import HttpResponse
from .models import ChaiVariety



# Create your views here.


def home(request):
  return render(request, 'app.html')



def all_chai(request):
  chais = ChaiVariety.objects.all()
  return render(request, 'chai/all_chai.html', {'chais': chais})