from django.urls import path, include
from rest_framework import routers
from .views import BudgetViewSet

router = routers.DefaultRouter()
router.register(r'budgets', BudgetViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
