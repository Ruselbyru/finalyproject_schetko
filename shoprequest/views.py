from django.shortcuts import render
from .models import Shoprequest
from django.views.generic.edit import CreateView
# Create your views here.


class ShoprequestView (CreateView):
    model = Shoprequest
    template_name = 'Shoprequest.html'
    fields = '__all__'