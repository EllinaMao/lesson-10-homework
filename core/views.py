from django.shortcuts import render
import json
import requests
import uuid
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

import azure.cognitiveservices.speech as speechsdk
from .helpers import *

# Create your views here.
def index(request):
    """Отображение главной страницы."""
    return render(request, "translator_app/index.html")

