from django.db import models

class Team(models.Model):
    """Model to represent a football team."""
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Player(models.Model):
    """Model to represent a player in a team."""
    POSITION_CHOICES = [
        ('GK', 'Goalkeeper'),
        ('DF', 'Defender'),
        ('MF', 'Midfielder'),
        ('FW', 'Forward'),
    ]

    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)
    age = models.PositiveIntegerField()
    nationality = models.CharField(max_length=50, default="Kenyan")

    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"

    class Meta:
        ordering = ['name']
