from vehicles import views
from django.urls import path

urlpatterns = [
    path('', views.result.as_view(), name='result'),
]
