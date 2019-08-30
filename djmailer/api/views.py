from rest_framework.viewsets import ModelViewSet

from .SubscriberSerializer import SubsciberSerializer
from .models import Subscriber


class SubscriberViewSet(ModelViewSet):
    serializer_class = SubsciberSerializer
    queryset = Subscriber.objects.all()


   


