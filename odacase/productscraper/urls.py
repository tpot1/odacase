from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('<int:configId>/run', views.productscraper, name='productscraper'),
]