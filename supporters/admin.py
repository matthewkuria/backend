from django.contrib import admin
from .models import MembershipTier, Supporter
# Register your models here.
admin.site.register(MembershipTier)
admin.site.register(Supporter)