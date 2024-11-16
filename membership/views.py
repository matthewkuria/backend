from django.conf import settings
from django.core.mail import send_mail, BadHeaderError
from django.utils.timezone import now
from rest_framework import status, permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Membership, MembershipPlan
from .serializers import MembershipPlanSerializer, MembershipSerializer
from datetime import timedelta
from .utils import send_confirmation_email



class MembershipPlanViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View to list available membership plans.
    """
    queryset = MembershipPlan.objects.all()
    serializer_class = MembershipPlanSerializer
    permission_classes = [permissions.AllowAny]  # Publicly accessible


class MembershipViewSet(viewsets.ModelViewSet):
    """
    View to handle the creation of memberships for authenticated users.
    """
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can create memberships

    def get_queryset(self):
        """
        Return memberships for the logged-in user only.
        """
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Override create to handle membership purchase and send an email.
        """
        # Extract plan_id from the request data
        plan_id = request.data.get('plan_id')
        if not plan_id:
            return Response({"detail": "Membership plan ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Fetch the plan from the database
            plan = MembershipPlan.objects.get(id=plan_id)
        except MembershipPlan.DoesNotExist:
            return Response({"detail": "Invalid membership plan."}, status=status.HTTP_400_BAD_REQUEST)

        # Calculate end_date based on the plan's duration
        end_date = now() + timedelta(days=plan.duration_in_days)

        # Create the membership
        membership = Membership.objects.create(
            user=request.user,
            plan=plan,
            end_date=end_date
        )

        # Send a confirmation email
        send_confirmation_email(
            user_email=request.user.email,
            plan=plan,
            end_date=end_date
        )

        # Serialize the created membership and return a success response
        serializer = self.get_serializer(membership)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


