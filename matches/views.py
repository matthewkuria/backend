from rest_framework import viewsets, permissions
from .models import Match, Team
from .serializers import MatchSerializer, TeamSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for listing, creating, retrieving, updating, and deleting teams."""
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]
