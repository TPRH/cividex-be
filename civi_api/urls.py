from django.urls import path
from .views import FactList, FactDetail


urlpatterns = [
  path('', FactList.as_view(), name='fact_list'),
  path('<int:pk>/', FactDetail.as_view(), name='fact_detail')
]
