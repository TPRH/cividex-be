from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Fact

class FactSerializer(serializers.ModelSerializer):
  class Meta:
    model = Fact
    fields = '__all__'
