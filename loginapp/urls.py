from django.urls import path
from . import views
urlpatterns=[
path('',views.index,name='index'),
path('login',views.login,name='login'),
path('registor',views.registor,name='registor'),
path('registration',views.registration,name='registration'),
]