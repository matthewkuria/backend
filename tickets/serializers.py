from rest_framework import serializers
from .models import Ticket
from matches.serializers import MatchSerializer


class TicketSerializer(serializers.ModelSerializer):
    qr_code_image_url = serializers.ImageField(source='qr_code_image', read_only=True)
    
    match = MatchSerializer()

    class Meta:
        model = Ticket
        fields = ['id', 'match', 'price', 'status', 'qr_code_data', 'qr_code_image_url']
