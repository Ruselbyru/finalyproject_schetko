from django.urls import path
from . import views


urlpatterns = [
    path('shoprequest', views.ShoprequestView.as_view(), name='shoprequest'),
]