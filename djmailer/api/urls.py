from django.urls import path
from .views import SubscriberView
from .views import helloWorldView2


app_name = 'api'

urlpatterns = [
    path('subscriber', SubscriberView.as_view(), name='subscriber'),
    path('hello2', helloWorldView2, name="helloWorld2")
]
