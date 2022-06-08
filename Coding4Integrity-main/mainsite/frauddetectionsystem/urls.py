from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('investigation', views.investigation, name='investigation'),
    path('ussd', views.ussd, name='ussd'),
    path('user', views.user, name='user'),
    path('mlmodel', views.mlmodel, name='mlmodel'),
]