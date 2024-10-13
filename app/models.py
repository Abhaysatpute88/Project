from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    question_text = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    difficulty = models.IntegerField(default=1)  # 1: easy, 2: medium, 3: hard

    def __str__(self):
        return self.question_text

class Player(models.Model):
    player_id = models.CharField(max_length=255, unique=True) 
    score = models.IntegerField(default=0)
    streak = models.IntegerField(default=0)

    def __str__(self):
        return self.player_id

class GameSession(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answered_correctly = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
