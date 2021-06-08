from django.shortcuts import render
from rest_framework import generics
from .serializers import MainAppDetailSerializer, MainAppListSerializer
from .models import ListAll
# Create your views here.


class MainAppCreateVew(generics.CreateAPIView):
    serializer_class = MainAppDetailSerializer


class MainAppListView(generics.ListAPIView):
    serializer_class = MainAppListSerializer
    queryset = ListAll.objects.all()


class MainAppDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MainAppDetailSerializer
    queryset = ListAll.objects.all()
