from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import BrandAuto, ModelAuto, ClientRequest
from .forms import ClientRequestForm

# Create your views here.


class ClientRequestCreateView (CreateView):
    model = ClientRequest
    template_name = 'Clientrequest.html'
    form_class = ClientRequestForm

def models_for_brand (request):
    if request.GET.get ('brandauto'):
        brand = int(request.GET.get ('brandauto'))
        models = ModelAuto.objects.filter (brandauto_id=brand)
    else:
        models = [None]
    return render (request, 'model_for_brand.html',{'models':models})


