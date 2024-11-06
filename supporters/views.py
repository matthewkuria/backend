from rest_framework import viewsets, permissions
from .models import Supporter, MembershipTier
from .serializers import SupporterSerializer, MembershipTierSerializer

class MembershipTierViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, creating, retrieving, updating, and deleting membership tiers."""
    queryset = MembershipTier.objects.all()
    serializer_class = MembershipTierSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]  # Allow read for all, restrict create/edit

class SupporterViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, creating, retrieving, updating, and deleting supporters."""
    queryset = Supporter.objects.all()
    serializer_class = SupporterSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        """Override perform_create to automatically set the user from the request."""
        serializer.save(user=self.request.user)
