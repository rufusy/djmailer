from rest_framework import serializers

class SubsciberSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=6)
    age = serializers.IntegerField()
    email = serializers.EmailField()
