from rest_framework import serializers
from .models import User, Address

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    address_line_two = serializers.CharField(required=False, default='')
    class Meta:
        model = Address
        fields = "__all__"

class UserFullySerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)
    class Meta:
        model = User
        fields = "__all__"