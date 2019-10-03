from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, generics
from rest_framework_jwt.settings import api_settings
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import Http404
from django.contrib.auth import login as django_login, logout as django_logout
from FRS.serializers import FlightSerializer, UserSerializer, TokenSerializer
from FRS.models import Flight
from FRS.utils import SetPagination


jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER


class LoginView(generics.CreateAPIView):
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username", "")
        password = request.data.get("password", "")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            serializer = TokenSerializer(
                data={"token": jwt_encode_handler(jwt_payload_handler(user))})
            serializer.is_valid()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({'message': username}, status=status.HTTP_404_NOT_FOUND)


class UserCreate(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                token = Token.objects.create(user=user)
                json = serializer.data
                json['token'] = token.key
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightList(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)

    serializer_class = FlightSerializer
    queryset = Flight.objects.all()
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('name', 'scheduled_date', 'departure', 'destination')
    ordering_fields = ('fare', 'name')
    ordering = ('scheduled_date',)
    pagination_class = SetPagination

    def post(self, request):
        """add flight info"""
        serializer = FlightSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FlightDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get_object(self, pk):
        try:
            return Flight.objects.get(pk=pk)
        except:
            raise Http404

    def post(self, request, pk):
        """update flight info"""
        flight = self.get_object(pk)
        serializer = FlightSerializer(flight, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        """remove flight info"""
        flight = self.get_object(pk)
        flight.delete()
        return Response(status=status.HTTP_200_OK)
