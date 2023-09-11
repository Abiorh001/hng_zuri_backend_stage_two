from rest_framework import serializers
from .models import ZuriApisModel


class ZuriSerializer(serializers.ModelSerializer):
    class Meta:
        model = ZuriApisModel
        fields = '__all__'
