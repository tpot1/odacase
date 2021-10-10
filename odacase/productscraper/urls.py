from django.urls import path
from . import views 

urlpatterns = [
    path('<int:configId>/run', views.productscraper, name='productscraper'),
]