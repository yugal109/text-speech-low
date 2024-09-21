
from django.urls import path
from .views import text_to_speech

app_name="ttsapp"
urlpatterns = [
    path('convert/',text_to_speech),
]
