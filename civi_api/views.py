import imp
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import FactSerializer
from .models import Fact


class FactList(ListCreateAPIView):
  queryset = Fact.objects.all()
  serializer_class = FactSerializer

class FactDetail(RetrieveUpdateDestroyAPIView):
  queryset = Fact.objects.all()
  serializer_class = FactSerializer
