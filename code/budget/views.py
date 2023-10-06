from rest_framework import viewsets
from .serializers import BudgetSerializer
from .models import Budget

# Create your views here.


class BudgetViewSet(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
