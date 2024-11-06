from django.urls import path
from . import payment_views

urlpatterns = [
    path('initialize/<int:ticket_id>/', payment_views.InitializePaymentView.as_view(), name='initialize-payment'),
    path('callback/', payment_views.PaymentCallbackView.as_view(), name='payment-callback'),
]
