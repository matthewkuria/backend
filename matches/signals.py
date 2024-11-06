from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Match
from .utils import update_team_standings  

@receiver(post_save, sender=Match)
def update_standings_on_match_save(sender, instance, **kwargs):
    update_team_standings(instance)
