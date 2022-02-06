from django.urls import path, include
from rest_framework import routers
from . import views 

router = routers.DefaultRouter()
router.register(r'config', views.psconfigView, 'config')
router.register(r'attribute', views.psattributeView, 'attribute')

urlpatterns = [
    path('', views.home, name='home'),
    path('new', views.new, name='new'),
    path('<int:configId>/run', views.productscraper, name='productscraper'),
    path('api/', include(router.urls)),
]