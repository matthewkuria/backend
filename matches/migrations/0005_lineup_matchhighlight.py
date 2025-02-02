# Generated by Django 5.1.1 on 2024-11-02 18:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matches', '0004_alter_match_options_alter_match_match_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lineup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_name', models.CharField(max_length=100)),
                ('position', models.CharField(max_length=50)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lineups', to='matches.match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matches.team')),
            ],
        ),
        migrations.CreateModel(
            name='MatchHighlight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minute', models.IntegerField()),
                ('event', models.CharField(max_length=255)),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='match_highlights', to='matches.match')),
            ],
        ),
    ]
