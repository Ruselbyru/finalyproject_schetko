from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import BrandAuto, ModelAuto, ClientRequest
from .forms import ClientRequestForm
from django.db.models.signals import post_save
from telegram_bot.management.commands.bot import Command

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




def testsiglan (sender, instance, created , **kwargs):
    name = instance.id
    # info= ClientRequest.objects.get (client_name=name)
    # print(info.brandauto)
    print(name)
    return created

post_save.connect(testsiglan,sender=ClientRequest)


