from django.db import models

  
  

class Player(models.Model):
    """Model to represent a player in a team."""
    TEAM_CHOICES = [
        ('stars','Ulinzi Stars'),
        ('starlets','Ulinzi Starlets'),
        ('youths','Ulinzi Youths'),
    ]
    POSITION_CHOICES = [
        ('GoalKeeper', 'Goalkeeper'),
        ('Defender', 'Defender'),
        ('Midfielder', 'Midfielder'),
        ('Striker', 'Striker'),
    ]
    STATUS_CHOICES =[
        ('military', 'Military'),
        ('civilian', 'Civilian')
    ]

    
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, choices=POSITION_CHOICES)
    age = models.PositiveIntegerField()
    image=models.ImageField(upload_to='player-images/', blank=True, null=True, default="default.png")
    team = models.CharField(max_length=100,choices=TEAM_CHOICES)
    status = models.CharField(max_length=50,choices=STATUS_CHOICES, default="military" )
    def __str__(self):
        return f"{self.name} - {self.get_position_display()}"

    class Meta:
        ordering = ['name']
