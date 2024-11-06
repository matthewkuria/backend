from django.contrib import admin
from .models import Ticket, Payment

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('match', 'price', 'status', 'user', 'created_at', 'updated_at')

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('ticket', 'user', 'amount', 'status', 'payment_reference', 'created_at', 'updated_at')
