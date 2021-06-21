from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import BrandAuto, ModelAuto, ClientRequest
# Create your views here.


class ClientRequestCreateView (CreateView):
    model = ClientRequest
    template_name = 'home.html'
    fields = '__all__'

