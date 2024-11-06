# payment_views.py
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Ticket, Payment
import requests

class InitializePaymentView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, ticket_id):
        """Initializes the payment process for a specific ticket."""
        try:
            # Fetch the ticket
            ticket = Ticket.objects.get(id=ticket_id, user=request.user)
            
            # External payment gateway payload
            payment_data = {
                "amount": ticket.price,  # or any amount logic based on ticket
                "currency": "USD",
                "redirect_url": f"{settings.FRONTEND_URL}/payment/callback/",
                "metadata": {
                    "ticket_id": ticket_id,
                    "user_id": request.user.id,
                }
            }

            # Replace this with actual API call to payment gateway
            payment_gateway_response = requests.post(
                "https://api.paymentgateway.com/v1/payments",
                json=payment_data
            )
            payment_info = payment_gateway_response.json()
            
            # Save payment reference or info to your DB
            Payment.objects.create(
                ticket=ticket,
                user=request.user,
                amount=ticket.price,
                status="pending",
                payment_reference=payment_info["id"]
            )

            # Redirect to the payment gateway URL
            return Response({"payment_url": payment_info["payment_url"]})

        except Ticket.DoesNotExist:
            return Response({"error": "Ticket not found or already purchased"}, status=404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)

class PaymentCallbackView(APIView):
    """Handles the payment callback from the payment gateway."""

    def get(self, request):
        payment_id = request.query_params.get("payment_id")
        payment_status = request.query_params.get("status")

        try:
            payment = Payment.objects.get(payment_reference=payment_id)
            payment.status = payment_status
            payment.save()

            if payment_status == "completed":
                # Mark ticket as purchased
                ticket = payment.ticket
                ticket.status = "purchased"
                ticket.save()

            return redirect(f"{settings.FRONTEND_URL}/payment/success/" if payment_status == "completed" else f"{settings.FRONTEND_URL}/payment/failed/")
        
        except Payment.DoesNotExist:
            return Response({"error": "Payment not found"}, status=404)
