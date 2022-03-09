from django.urls import path

from home.api.api_view import get_question, set_answer, get_user

urlpatterns = [
    path("questions/<int:pk>/", get_question),
    path('set-answer/<int:pk>/', set_answer),
    path('get-user/<int:pk>/', get_user),
]