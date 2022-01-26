from .models import Storecentre
from rest_framework import serializers

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Storecentre
        fields = ('name', 'description', 'price','no_of units')