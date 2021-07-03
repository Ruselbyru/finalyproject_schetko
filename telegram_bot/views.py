from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .newbot import write_json
import json



# Create your views here.
@csrf_exempt
def index (request, methods=['POST','GET']):
    if request.method == 'POST':
        r = json.loads(request.body.decode())
        # print(r)
        write_json(r)
    return render(request,'home.html')