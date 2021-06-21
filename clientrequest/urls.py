from django.urls import path
from . import views


urlpatterns = [
    path('', views.ClientRequestCreateView.as_view(), name='home'),

]