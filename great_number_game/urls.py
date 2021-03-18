from django.urls import path, include

urlpatterns = [
    path('', include('great_number_game_app.routes')),
]
