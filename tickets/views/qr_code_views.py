import qrcode
import io
from django.http import HttpResponse
from django.conf import settings
from ..models import Ticket

def generate_qr_code(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
        payment_url = f"{settings.FRONTEND_URL}/tickets/{ticket_id}/payment"
        
        qr = qrcode.make(payment_url)
        buffer = io.BytesIO()
        qr.save(buffer, format="PNG")
        buffer.seek(0)

        return HttpResponse(buffer, content_type="image/png")
    except Ticket.DoesNotExist:
        return HttpResponse("Ticket not found", status=404)
