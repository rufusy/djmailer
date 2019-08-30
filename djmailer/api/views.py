from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.status import HTTP_400_BAD_REQUEST

from .SubscriberSerializer import SubsciberSerializer
from .models import Subscriber
 

class SubscriberView(APIView):
    def get(self, request):
        allSubscribers = Subscriber.objects.all()
        serializedSubscribers = SubsciberSerializer(allSubscribers, many=True)
        return Response(serializedSubscribers.data)
     
    def post(self, request):
        serializer = SubsciberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber_instance = Subscriber.objects.create(**serializer.data)
            return Response({"message":"Created susbscriber {}".format(subscriber_instance.id)})
        else:
            return Response({"errors":serializer.errors}, status=HTTP_400_BAD_REQUEST)


@api_view(["GET", "POST"])
def helloWorldView2(request):
    if request.method == "GET":
        return Response({"message":"Hello world"})
    
    else:
        name = request.data.get("name")
        if not name:
            return Response({"error":"No name passed"}, status=HTTP_400_BAD_REQUEST)
        return Response({"message":"Hello {}!".format(name)})