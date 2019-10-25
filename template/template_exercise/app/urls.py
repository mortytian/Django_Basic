from django.urls import path
from .views import exercise

urlpatterns = [
    path('exercise/<str:message_type>', exercise.as_view(), name='exercise')
]