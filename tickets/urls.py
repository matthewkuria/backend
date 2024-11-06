from django.urls import path
from .views.ticket_views import TicketViewSet
from .views.qr_code_views import generate_qr_code

ticket_viewset = TicketViewSet.as_view({
    'get': 'retrieve',
    'post': 'purchase'
})

urlpatterns = [
    path('<int:pk>/', ticket_viewset, name='ticket_detail'),
    path('<int:pk>/purchase/', ticket_viewset, name='ticket_purchase'),
    path('<int:ticket_id>/qr_code/', generate_qr_code, name='generate_qr_code'),
]
