from rest_framework import serializers
from rest_framework import serializers
from .models import Match, Team, TeamStanding, Lineup, MatchHighlight

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['id', 'name', 'logo']


class TeamStandingSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = TeamStanding
        fields = [
            'id', 'team', 'points', 'goals_scored',
            'goals_conceded', 'games_played', 'wins', 'draws', 'losses'
        ]


class LineupSerializer(serializers.ModelSerializer):
    team = TeamSerializer()

    class Meta:
        model = Lineup
        fields = ['id', 'team', 'player_name', 'position']


class MatchHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = MatchHighlight
        fields = ['id', 'minute', 'event']


class MatchSerializer(serializers.ModelSerializer):
    """Serializer for the Match model."""    
    home_team = TeamSerializer()
    away_team = TeamSerializer()
    team_standings = TeamStandingSerializer(many=True, read_only=True)
    lineups = LineupSerializer(many=True, read_only=True)
    match_highlights = MatchHighlightSerializer(many=True, read_only=True)

    class Meta:
        model = Match
        fields = [
            'id', 'home_team', 'away_team', 'stadium', 'match_date',
            'home_score', 'away_score', 'league', 'team_standings', 'lineups', 'match_highlights'
        ]
    def create(self, validated_data):
        """Override create method to return the match instance."""
        match = Match(**validated_data)
        match.save()
        return match
