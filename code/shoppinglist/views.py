from rest_framework import viewsets
from .models import ShoppingList
from .serializers import ShoppingListSerializer

# Create your views here.


class ShoppingListViewSet(viewsets.ModelViewSet):
    queryset = ShoppingList.objects.all()
    serializer_class = ShoppingListSerializer
