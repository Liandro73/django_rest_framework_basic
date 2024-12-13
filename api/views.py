from django.db.models import Q
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Address
from .serializer import UserSerializer, UserFullySerializer, AddressSerializer


@api_view(['GET'])
def get_users(request):
    users = User.objects.select_related()
    serializer = UserFullySerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_users_by_search(request, search):
    transactions = User.objects.filter( Q(id__icontains=search) | Q(name__icontains=search) | Q(age__icontains=search) )
    transactions_serializer = UserSerializer(transactions, many=True)
    return Response(transactions_serializer.data)

@api_view(['POST'])
def create_user(request):
    users_serializer = UserSerializer(data=request.data)
    if users_serializer.is_valid():
        users_serializer.save()
        return Response(users_serializer.data, status=status.HTTP_201_CREATED)
    return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def manipulate_user(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        users_serializer = UserSerializer(user)
        return Response(users_serializer.data)

    elif request.method == 'PUT':
        users_serializer = UserSerializer(user, data=request.data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response(users_serializer.data)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def get_addresses(request):
    address = Address.objects.all()
    serializer = AddressSerializer(address, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_address(request):
    addresses_serializer = AddressSerializer(data=request.data)
    if addresses_serializer.is_valid():
        addresses_serializer.save()
        return Response(addresses_serializer.data, status=status.HTTP_201_CREATED)
    return Response(addresses_serializer.errors, status=status.HTTP_400_BAD_REQUEST)