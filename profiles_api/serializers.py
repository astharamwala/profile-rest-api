from rest_framework import serializers


class HelloSerializer(serializers.Serializer):
    """manage serializers"""
    name = serializers.CharField(max_length=10)