from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import QuestionViewSet, PlayerViewSet, GameSessionViewSet

router = DefaultRouter()
router.register(r'questions', QuestionViewSet, basename='question')
router.register(r'players', PlayerViewSet, basename='player')
router.register(r'sessions', GameSessionViewSet, basename='session')

urlpatterns = [
    path('', include(router.urls)),
]
