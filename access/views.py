from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        if User.objects.filter(username=username).exists():
            return Response({"error": "User exists"}, status=400)

        user = User.objects.create_user(username=username, password=password)
        return Response({"message": "User created"}, status=201)
