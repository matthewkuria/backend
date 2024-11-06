from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class MembershipTier(models.Model):
    """Model to represent a membership tier for supporters."""
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    points_needed = models.IntegerField()

    def __str__(self):
        return self.name

class Supporter(models.Model):
    """Model to represent a supporter of the football club."""
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='supporter')
    membership_tier = models.ForeignKey(MembershipTier, on_delete=models.SET_NULL, null=True, blank=True)
    loyalty_points = models.IntegerField(default=0)
    joined_date = models.DateField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username} - {self.membership_tier.name if self.membership_tier else 'No Tier'}"
