from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import BrandAuto, ModelAuto, ClientRequest
from .forms import ClientRequestForm

# Create your views here.


class ClientRequestCreateView (CreateView):
    model = ClientRequest
    template_name = 'home.html'
    form_class = ClientRequestForm

def models_for_brand (request):
    if request.GET.get ('brandauto'):
        brand = int(request.GET.get ('brandauto'))
        models = BrandAuto.objects.get (id=brand).modelauto_set.all()
    else:
        models = []
    return render (request, 'model_for_brand.html',{'models':models})


