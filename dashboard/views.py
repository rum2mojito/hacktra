from django.shortcuts import render
from django.http import HttpResponse

import datetime

# Create your views here.

def hello_world(request):
  return render(request, 'hello_world.html', {
    'current_time': str(datetime.time()),
  })
