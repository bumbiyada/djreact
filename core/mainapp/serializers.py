from rest_framework import serializers
from .models import ListAll


class MainAppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = '__all__'


class MainAppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = '__all__'