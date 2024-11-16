from django.urls import path
from .views import MembershipPlanViewSet, MembershipViewSet

urlpatterns = [
    path('plans/', MembershipPlanViewSet.as_view({'get': 'list'}), name='membership-plans'),
    path('my-memberships/', MembershipViewSet.as_view({'get': 'list'}), name='my-memberships'),
]
