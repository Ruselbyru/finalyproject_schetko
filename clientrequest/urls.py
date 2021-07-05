from django.urls import path
from . import views


urlpatterns = [
    path('clientrequest', views.ClientRequestCreateView.as_view(), name='clientrequest'),
    path('model_for_brand/', views.models_for_brand),
    path('goodrequest/', views.goodrequest, name = 'goodrequest'),

]