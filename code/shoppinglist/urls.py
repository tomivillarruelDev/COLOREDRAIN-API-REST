from django.urls import path, include
from rest_framework import routers
from .views import ShoppingListViewSet

router = routers.DefaultRouter()
router.register(r'shoppinglist', ShoppingListViewSet)

urlpatterns = [
    path('', include(router.urls))
]
