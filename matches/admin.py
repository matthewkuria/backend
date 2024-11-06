from django.contrib import admin
from .models import Team, Match, League, TeamStanding, Lineup, MatchHighlight

# Register your models here.
admin.site.register(Team)
admin.site.register(Match)
admin.site.register(League)
admin.site.register(TeamStanding)
admin.site.register(Lineup)
admin.site.register(MatchHighlight)