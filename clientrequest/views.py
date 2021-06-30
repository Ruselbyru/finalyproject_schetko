from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import BrandAuto, ModelAuto, ClientRequest
from .forms import ClientRequestForm
from django.db.models.signals import post_save

# Create your views here.


class ClientRequestCreateView (CreateView):
    model = ClientRequest
    template_name = 'Clientrequest.html'
    form_class = ClientRequestForm

def testsiglan (sender, instance, created , **kwargs):
    name = instance.id
    # info= ClientRequest.objects.get (client_name=name)
    # print(info.brandauto)
    print(name)


post_save.connect(testsiglan,sender=ClientRequest)

def models_for_brand (request):
    if request.GET.get ('brandauto'):
        brand = int(request.GET.get ('brandauto'))
        models = ModelAuto.objects.filter (brandauto_id=brand)
    else:
        models = [None]
    return render (request, 'model_for_brand.html',{'models':models})


