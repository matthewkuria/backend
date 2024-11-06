from django.db import transaction
from .models import TeamStanding

def update_team_standings(match):
    """
    Update the standings for both the home and away teams after a match.
    """
    try:
        # Ensure the operation is atomic to prevent partial updates
        with transaction.atomic():
            # Get or create standings for home and away teams
            home_team_standing, created = TeamStanding.objects.get_or_create(
                team=match.home_team,
                league=match.league
            )
            away_team_standing, created = TeamStanding.objects.get_or_create(
                team=match.away_team,
                league=match.league
            )

            # Update standings for home and away teams
            home_team_standing.update_stats(match)
            away_team_standing.update_stats(match)

    except Exception as e:
        # Log the exception if necessary
        print(f"Error updating team standings: {e}")
