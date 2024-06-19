from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PizzaViewSet

router = DefaultRouter()
router.register(r'pizzas', PizzaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]