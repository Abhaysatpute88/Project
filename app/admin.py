from django.contrib import admin
from .models import Question, Player, GameSession

# Register the Question model with the admin interface
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'difficulty')  # Columns to display in the admin list view
    search_fields = ('question_text',)  # Allow search by question text
    list_filter = ('difficulty',)  # Filter questions by difficulty level

# Register the Player model with the admin interface
@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('player_id', 'score', 'streak')  # Display user, score, and streak
    search_fields = ('user__username',)  # Allow search by username
    list_filter = ('score',)  # Filter players by score

# Register the GameSession model with the admin interface
@admin.register(GameSession)
class GameSessionAdmin(admin.ModelAdmin):
    list_display = ('player', 'question', 'answered_correctly', 'timestamp')  # Display player, question, and if answered correctly
    list_filter = ('answered_correctly', 'timestamp')  # Filter by answer correctness and timestamp
    search_fields = ('player__user__username', 'question__question_text')  # Allow search by player's username and question text
