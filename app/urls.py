from django.urls import path
from .views import *

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/my/', UserProjectsView.as_view(), name='user-projects'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail')
]
