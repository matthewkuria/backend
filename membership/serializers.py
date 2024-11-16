from rest_framework import serializers
from .models import MembershipPlan, Membership

class MembershipPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipPlan
        fields = ['id', 'name', 'description', 'price', 'duration_in_days']

class MembershipSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)  # Displays user's email/username
    plan = MembershipPlanSerializer(read_only=True)
    plan_id = serializers.PrimaryKeyRelatedField(
        queryset=MembershipPlan.objects.all(), write_only=True, source='plan'
    )

    class Meta:
        model = Membership
        fields = ['id', 'user', 'plan', 'plan_id', 'start_date', 'end_date', 'is_active']
        read_only_fields = ['start_date', 'end_date', 'is_active']

    def create(self, validated_data):
        user = self.context['request'].user  # Automatically assign the logged-in user
        validated_data['user'] = user
        return super().create(validated_data)
