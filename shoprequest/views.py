from django.shortcuts import render
from .models import Shoprequest
from django.views.generic.edit import CreateView
# Create your views here.

# Отображение на странице формы, для регистрации Магазина
class ShoprequestView (CreateView):
    model = Shoprequest
    template_name = 'Shoprequest.html'
    fields = '__all__'

def goodshop (reaquest):
    return render(reaquest, 'goodshop.html')