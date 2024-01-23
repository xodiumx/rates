from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import Rates

from .serializers import RatesSerializer


class RatesViewSet(ListModelMixin, GenericViewSet):

    queryset = Rates.objects.all()
    http_method_names = ('get',)
    serializer_class = RatesSerializer
    