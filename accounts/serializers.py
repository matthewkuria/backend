from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from fans.models import Fan

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(username=email, password=password)  # Use email as the username
            if not user:
                raise serializers.ValidationError('Invalid credentials')
        else:
            raise serializers.ValidationError('Both fields are required.')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    fan = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','email', 'is_admin', 'is_staff', 'fan']

    def get_fan(self, obj):
        try:
            fan = Fan.objects.get(user=obj)
            return {
                'id':member.id,
                'full_name': member.full_name,
                'membership':member.membership,
                'dob':member.dob,
                'gender':member.gender,
                'mobile': member.mobile,
                'date_joined': member.date_joined,
            }
        except Fan.DoesNotExist:
            return None