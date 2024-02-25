from django.shortcuts import render
from .forms import audioform


def index(request):
   form = audioform(request.POST or None)
   if request is not None:
         msg = 'Valid'
   else:
         msg = 'Invalid'
   return render(request, 'home/index.html', {"text": msg})