import json
from django.http import JsonResponse
from django.views import View
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from .helpers import speech_to_text, text_to_speach, text_to_translate

from django.views import View
from django.views.generic import TemplateView


# Create your views here.
from django.shortcuts import render
from django.views import View
from .forms import TranslationForm
from .helpers import text_to_translate
class IndexView(View):
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        form = TranslationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TranslationForm(request.POST)
        translated_text = ""
        error_message = None

        if form.is_valid():
            text = form.cleaned_data.get('source_text', '')
            target_lang = form.cleaned_data.get('target_lang', 'en')

            if text:
                result = text_to_translate.translate_text(text, target_lang)
                if result.get("success"):
                    translated_text = result["translated_text"]
                else:
                    error_message = result.get("error")

        return render(request, self.template_name, {
            'form': form,
            'translated_text': translated_text,
            'error_message': error_message
        })
    
@method_decorator(csrf_exempt, name="dispatch")
class RecognizeSpeechView(View):

    def post(self, request, *args, **kwargs):
        result = speech_to_text.recognize_from_mic(language="ru-RU")

        if result.get("success"):
            return JsonResponse({"text": result["text"]})
        return JsonResponse({"error": result.get("error")}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class TranslateTextView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        text = data.get("text", "")
        target_lang = data.get("target_lang", "en")

        result = text_to_translate.translate_text(text, target_lang)

        if result.get("success"):
            return JsonResponse({"translated_text": result["translated_text"]})
        return JsonResponse({"error": result.get("error")}, status=400)


@method_decorator(csrf_exempt, name="dispatch")
class SynthesizeSpeechView(View):

    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        text = data.get("text", "")
        lang = data.get("lang", "en-US")

        result = text_to_speach.speak_text(text, lang)

        if result.get("success"):
            return JsonResponse({"status": "success"})
        return JsonResponse({"error": result.get("error")}, status=400)
