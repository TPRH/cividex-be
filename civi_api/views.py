from rest_framework.generics import generics
from .permissions import IsOwnerOrReadOnly
from .serializers import FactSerializer
from .models import Fact


class FactList(generics.ListCreateAPIView):
  queryset = Fact.objects.all()
  serializer_class = FactSerializer

class FactDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = (IsOwnerOrReadOnly, )
  queryset = Fact.objects.all()
  serializer_class = FactSerializer


