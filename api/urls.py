from django.urls import path, include
from rest_framework.routers import DefaultRouter
from news.views import NewsViewSet, NewsCategoryViewSet
from matches.views import TeamViewSet, MatchViewSet
from membership.views import MembershipPlanViewSet, MembershipViewSet
from supporters.views import SupporterViewSet, MembershipTierViewSet
from club.views import PlayerViewSet
from shop.views import ProductViewSet




router = DefaultRouter()
router.register(r'news', NewsViewSet)
router.register(r'categories', NewsCategoryViewSet)
router.register(r'teams', TeamViewSet, basename='team')
router.register(r'matches', MatchViewSet, basename='match')
router.register(r'membership-plans', MembershipPlanViewSet, basename='membership-plan')
router.register(r'memberships', MembershipViewSet, basename='membership')
router.register(r'membership-tiers', MembershipTierViewSet, basename='membershiptier')
router.register(r'supporters', SupporterViewSet, basename='supporter')
router.register(r'players', PlayerViewSet)
router.register(r'shop', ProductViewSet)



urlpatterns = [
path('', include(router.urls)),

]
