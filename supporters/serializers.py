from rest_framework import serializers
from .models import Supporter, MembershipTier
from django.contrib.auth import get_user_model

User = get_user_model()

class MembershipTierSerializer(serializers.ModelSerializer):
    """Serializer for the MembershipTier model."""
    class Meta:
        model = MembershipTier
        fields = ['id', 'name', 'description', 'benefits', 'points_needed']

class SupporterSerializer(serializers.ModelSerializer):
    """Serializer for the Supporter model."""
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())  # Reference the User model
    membership_tier = MembershipTierSerializer(read_only=True)

    class Meta:
        model = Supporter
        fields = ['id', 'user', 'membership_tier', 'loyalty_points', 'joined_date', 'active']
        read_only_fields = ['joined_date', 'loyalty_points']

    def create(self, validated_data):
        """Override create method to create a supporter with a user."""
        user = validated_data.get('user')
        supporter, created = Supporter.objects.get_or_create(user=user, defaults=validated_data)
        return supporter
