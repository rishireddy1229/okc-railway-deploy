# -*- coding: utf-8 -*-
"""Contains models related to stats"""
from django.db import models

class Player(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=100)
    team = models.CharField(max_length=50)
    position = models.CharField(max_length=10)
    height = models.FloatField(null=True)
    weight = models.FloatField(null=True)

    def __str__(self):
        return self.full_name


class Game(models.Model):
    id = models.IntegerField(primary_key=True)
    date = models.DateField()

    def __str__(self):
        return f"Game {self.id} on {self.date}"


class Shot(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    shot_made = models.BooleanField()
    points = models.IntegerField()
    loc_x = models.FloatField()
    loc_y = models.FloatField()

    def __str__(self):
        return f"Shot {self.id} by {self.player.full_name}"


class Pass(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    completed_pass = models.BooleanField()
    potential_assist = models.BooleanField()
    turnover = models.BooleanField()
    ball_start_loc_x = models.FloatField()
    ball_start_loc_y = models.FloatField()
    ball_end_loc_x = models.FloatField()
    ball_end_loc_y = models.FloatField()

    def __str__(self):
        return f"Pass {self.id} by {self.player.full_name}"


class Turnover(models.Model):
    id = models.IntegerField(primary_key=True)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    action_type = models.CharField(max_length=50)
    loc_x = models.FloatField()
    loc_y = models.FloatField()

    def __str__(self):
        return f"Turnover {self.id} by {self.player.full_name}"