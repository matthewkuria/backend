from django.db import models
from django.conf import settings
from datetime import timedelta
from django.utils import timezone

class MembershipPlan(models.Model):
    """
    Represents the different membership plans available for purchase.
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_in_days = models.PositiveIntegerField(help_text="Duration of the plan in days")

    def __str__(self):
        return f"{self.name} (Ksh{self.price})"

class Membership(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE,
        related_name="memberships"
    )
    plan = models.ForeignKey(
        MembershipPlan, 
        on_delete=models.CASCADE,
        related_name="subscriptions"
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    is_active = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        # Ensure start_date is set to now if it's None
        if not self.start_date:
            self.start_date = timezone.now()
            
        # Automatically calculate the end_date based on the plan's duration
        if not self.end_date:
            self.end_date = self.start_date + timedelta(days=self.plan.duration_in_days)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.email} - {self.plan.name}"
