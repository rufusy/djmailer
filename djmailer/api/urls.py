from django.urls import path
from .views import SubscriberView


app_name = 'api'

urlpatterns = [
    path('subscriber', SubscriberView.as_view(), name='subscriber')
]
