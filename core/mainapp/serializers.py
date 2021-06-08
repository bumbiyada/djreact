from rest_framework import serializers
from .models import ListAll


class MainAppListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = ('id', 'Foiv', 'Stage_user')


class MainAppDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAll
        fields = '__all__'