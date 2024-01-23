from rest_framework.serializers import ModelSerializer

from .models import Rates


class RatesSerializer(ModelSerializer):

    class Meta:
        model = Rates
        fields = ('base_currency', 'current_currency', 'price', 'timestamp')
