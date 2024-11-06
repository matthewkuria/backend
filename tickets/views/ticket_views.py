from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Ticket
from ..serializers import TicketSerializer

class TicketViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def retrieve(self, request, pk=None):
        try:
            ticket = Ticket.objects.get(pk=pk)
            serializer = TicketSerializer(ticket)
            return Response(serializer.data)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket not found'}, status=status.HTTP_404_NOT_FOUND)

    def purchase(self, request, pk=None):
        try:
            ticket = Ticket.objects.get(pk=pk, status='available')
            ticket.status = 'purchased'
            ticket.purchaser = request.user
            ticket.save()
            return Response({'message': 'Ticket purchased successfully!'}, status=status.HTTP_200_OK)
        except Ticket.DoesNotExist:
            return Response({'error': 'Ticket not available'}, status=status.HTTP_404_NOT_FOUND)
