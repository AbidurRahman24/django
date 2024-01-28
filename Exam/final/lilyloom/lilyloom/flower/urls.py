from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views
router = DefaultRouter() 

router.register('list', views.FlowerCategoryViewset)
router.register('flower', views.FlowerCreateViewset)
router.register('order', views.OrderViewset)

urlpatterns = [
    path('', include(router.urls)),
]