from django.urls import path
from .views import *

app_name = 'mainapp'

urlpatterns = [
    path('mainapp/create', MainAppCreateVew.as_view()),
    path('mainapp/list', MainAppListView.as_view()),
    path('mainapp/detail/<int:pk>/', MainAppDetailView.as_view())
]

