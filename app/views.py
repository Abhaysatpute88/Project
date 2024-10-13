from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Question, Player, GameSession
from .serializers import QuestionSerializer, PlayerSerializer, GameSessionSerializer
from rest_framework.decorators import action

class QuestionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    @action(detail=False, methods=['get'])
    def random(self, request):
        question = Question.objects.order_by('?').first()
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

class PlayerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    @action(detail=False, methods=['get'])
    def leaderboard(self, request):
        players = Player.objects.order_by('-score')[:10]
        leaderboard = [{'userid': p.player_id, 'score': p.score} for p in players]
        return Response({'leaderboard': leaderboard})





class GameSessionViewSet(viewsets.ModelViewSet):
    queryset = GameSession.objects.all()
    serializer_class = GameSessionSerializer

    @action(detail=True, methods=['post'])
    def answer(self, request, pk=None):
        # Get the player_id from the request data
        player_id = request.data.get('player_id')
        if not player_id:
            return Response({"error": "player_id is required"}, status=400)

        # Retrieve or create a Player by player_id
        player, created = Player.objects.get_or_create(player_id=player_id)

        # Get the question by ID
        question = get_object_or_404(Question, id=pk)

        # Get the answer from the request data
        submitted_answer = request.data.get('answer')

        # Check if the answer is correct
        correct = submitted_answer.lower() == question.answer.lower()

        # Create a new GameSession entry
        session = GameSession.objects.create(
            player=player,
            question=question,
            answered_correctly=correct
        )

        # Update player's score and streak if correct
        if correct:
            player.score += 10  # Increment score
            player.streak += 1  # Increment streak
        else:
            player.streak = 0  # Reset streak if incorrect

        player.save()

        return Response({
            "answered_correctly": correct,
            "current_score": player.score,
            "streak": player.streak
        })
    








