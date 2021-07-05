from django.shortcuts import render
from django.views.generic.edit import CreateView
from .models import ModelAuto, ClientRequest
from .forms import ClientRequestForm
from django.db.models.signals import post_save
from telegram_bot.newbot import send_message
from telegram_bot.models import Shop_telegram


# Create your views here.
# Отображаем форму для клиентского запроса
class ClientRequestCreateView (CreateView):
    model = ClientRequest
    template_name = 'Clientrequest.html'
    form_class = ClientRequestForm


# страница для подгрузки определенного списка моделей в зависимости от марки
def models_for_brand (request):
    if request.GET.get ('brandauto'):
        brand = int(request.GET.get ('brandauto'))
        models = ModelAuto.objects.filter (brandauto_id=brand)
    else:
        models = [None]
    return render (request, 'model_for_brand.html',{'models':models})

def goodrequest (reaquest):
    return render(reaquest, 'goodrequest.html')


# Cлушаем сигнал о сохранении в БД Заявки и обрабатываем,
# Вызова фн, рассылки с проверкой состояния подписки на данную рассылку в Телеграме.
def testsiglan (sender, instance, created , **kwargs):
    message = f'НОВАЯ ЗАЯВКА!\nИмя: {instance.client_name}\nМарка автомобиля: {instance.brandauto}\nМодель автомобиля: {instance.modelauto}\n' \
              f'Год выпуска автомобиля: {instance.year_auto}\nЗапчасти: {instance.client_request}\nНомер телефона: {instance.client_phone}'
    for telegram_id in Shop_telegram.objects.filter(subscribe=True):
        send_message(chat_id=str(telegram_id),text=message)
    return created

post_save.connect(testsiglan,sender=ClientRequest)


