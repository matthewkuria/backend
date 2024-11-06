from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Ticket, Match
from .serializers import TicketSerializer, MatchSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class TicketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        ticket = get_object_or_404(Ticket, pk=pk)
        serializer = self.get_serializer(ticket)
        return Response(serializer.data, status=status.HTTP_200_OK)

class MatchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes =[IsAuthenticatedOrReadOnly]