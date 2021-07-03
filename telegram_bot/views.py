from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .newbot import write_json
from django.http import HttpRequest



# Create your views here.
@csrf_exempt
def index (request, methods=['POST','GET']):
    if request.method == 'POST':
        r = request.body.decode()
        print(r)
        write_json(r)
    return render(request,'home.html')