from django.db import models

class Team(models.Model):
    """Model to represent a football team."""
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='team_logos/', blank=True, null=True)

    def __str__(self):
        return self.name

class League(models.Model):
    """Model to represent a league or tournament."""
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100, blank=True, null=True)
    season = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.season})"

class Match(models.Model):
    """Model to represent a football match."""
    home_team = models.ForeignKey(
        'matches.Team',
        related_name='home_team_matches',
        on_delete=models.CASCADE
    )
    away_team = models.ForeignKey(
        'matches.Team',
        related_name='away_team_matches',
        on_delete=models.CASCADE
    )
    match_date = models.DateTimeField()  # Use DateField for unique date constraint
    stadium = models.CharField(max_length=50, null=True, blank=True)
    home_score = models.PositiveIntegerField(default=0)
    away_score = models.PositiveIntegerField(default=0)
    league = models.ForeignKey(
        League,
        related_name='matches',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    class Meta:
        # Enforce unique matches between the same teams on the same date
        unique_together = ('home_team', 'away_team', 'match_date')
        ordering = ['match_date']
    def __str__(self):
        return f"{self.home_team} vs {self.away_team} - {self.league.name if self.league else 'Friendly'}"

    @property
    def is_draw(self):
        """Returns True if the match is a draw."""
        return self.home_score == self.away_score

    @property
    def winner(self):
        """Returns the team with the higher score or None if it's a draw."""
        if self.home_score > self.away_score:
            return self.home_team
        elif self.away_score > self.home_score:
            return self.away_team
        return None

class Lineup(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE, related_name='lineups')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    player_name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.player_name} - {self.position} for {self.team.name}"


class MatchHighlight(models.Model):
    match = models.ForeignKey('Match', on_delete=models.CASCADE, related_name='match_highlights')
    minute = models.IntegerField()
    event = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.minute}': {self.event}"

class TeamStanding(models.Model):
    """Model to represent the standings for teams in a league."""
    team = models.OneToOneField('matches.Team', on_delete=models.CASCADE, related_name='standing')
    league = models.ForeignKey('matches.League', on_delete=models.CASCADE, related_name='standings')
    games_played = models.PositiveIntegerField(default=0)
    wins = models.PositiveIntegerField(default=0)
    draws = models.PositiveIntegerField(default=0)
    losses = models.PositiveIntegerField(default=0)
    goals_scored = models.PositiveIntegerField(default=0)
    goals_conceded = models.PositiveIntegerField(default=0)
    goal_difference = models.IntegerField(default=0)
    points = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-points', '-goal_difference', '-goals_scored']

    def save(self, *args, **kwargs):
        """Override save to update goal difference before saving."""
        self.goal_difference = self.goals_scored - self.goals_conceded
        super().save(*args, **kwargs)

    def update_stats(self, match):
        """Update standings based on the outcome of a match."""
        if match.home_team == self.team or match.away_team == self.team:
            if match.home_team == self.team:
                self.goals_scored += match.home_score
                self.goals_conceded += match.away_score
                if match.home_score > match.away_score:
                    self.wins += 1
                    self.points += 3
                elif match.home_score == match.away_score:
                    self.draws += 1
                    self.points += 1
                else:
                    self.losses += 1
            else:
                self.goals_scored += match.away_score
                self.goals_conceded += match.home_score
                if match.away_score > match.home_score:
                    self.wins += 1
                    self.points += 3
                elif match.home_score == match.away_score:
                    self.draws += 1
                    self.points += 1
                else:
                    self.losses += 1

            self.games_played += 1
            self.goal_difference = self.goals_scored - self.goals_conceded  # Update goal difference
            self.save()
