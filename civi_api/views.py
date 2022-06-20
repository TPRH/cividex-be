from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsOwnerOrReadOnly
from .serializers import FactSerializer
from .models import Fact


class FactList(ListCreateAPIView):
  queryset = Fact.objects.all()
  serializer_class = FactSerializer

class FactDetail(RetrieveUpdateDestroyAPIView):
  queryset = Fact.objects.all()
  serializer_class = FactSerializer
  permission_classes = (IsOwnerOrReadOnly, )
