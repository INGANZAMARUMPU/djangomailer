from rest_framework import serializers
from .models import *

class EmailSerializer(serializers.ModelSerializer):
    to = serializers.ListField(
        child=serializers.CharField()
    )
    class Meta:
        model = Email
        fields = "__all__"

class EmailOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Email
        fields = "__all__"