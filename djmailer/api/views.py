from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.generics import ListCreateAPIView

from .SubscriberSerializer import SubsciberSerializer
from .models import Subscriber
 
class SubscriberView(ListCreateAPIView):
    serializer_class = SubsciberSerializer
    queryset = Subscriber.objects.all()
    

    # def get(self, request):
    #     allSubscribers = Subscriber.objects.all()
    #     serializedSubscribers = SubsciberSerializer(allSubscribers, many=True)
    #     return Response(serializedSubscribers.data)
     
    # def post(self, request):
    #     serializer = SubsciberSerializer(data=request.data)
    #     if serializer.is_valid():
    #         subscriber_instance = Subscriber.objects.create(**serializer.data)
    #         return Response({"message":"Created susbscriber {}".format(subscriber_instance.id)})
    #     else:
    #         return Response({"errors":serializer.errors}, status=HTTP_400_BAD_REQUEST)


