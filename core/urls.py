from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("api/recognize/", views.RecognizeSpeechView.as_view(), name="recognize"),
    path("api/translate/", views.TranslateTextView.as_view(), name="translate"),
    path("api/synthesize/", views.SynthesizeSpeechView.as_view(), name="synthesize"),
]
