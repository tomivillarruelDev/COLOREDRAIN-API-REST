from rest_framework import serializers
from .models import Customer

# Serializers define the API representation.


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'lastname', 'phone']
