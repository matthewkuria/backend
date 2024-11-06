from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from .serializers import UserSerializer, UserProfileSerializer
from .models import CustomUser
from .permissions import IsAdmin

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny
from rest_framework import status 

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from .serializers import UserSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        
        if serializer.is_valid():
            user = serializer.save()
            return Response({'message': "User created and Fan profile linked."}, status=status.HTTP_201_CREATED)
        
        # If there are validation errors, return them with a 400 status
        return Response({
            'errors': serializer.errors,
            'message': "Please check the input fields."
        }, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(email=email, password=password)

        if user:
            # Create JWT token
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            # Determine redirect URL based on user role
            if user.is_admin:
                redirect_url = '/dashboard/'  # Admin Dashboard
            else:
                redirect_url = '/fan-dashboard/'  # Fan Dashboard

            # Return the token and redirect URL
            return Response({
                'refresh': str(refresh),
                'access': access_token,
                'redirect_url': redirect_url
            }, status=status.HTTP_200_OK)

        # If authentication fails, return an error response
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)


