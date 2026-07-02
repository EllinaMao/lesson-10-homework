"pip install azure-cognitiveservices-speech"

import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential

from . import utils as u

def recognize_from_mic(language="ru-RU"):
    try:
        AZURE_URL, AZURE_KEY, AZURE_REGION = u.get_creds()
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_KEY, region=AZURE_REGION
        )
        speech_config.speech_recognition_language = language

        recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)
        result = recognizer.recognize_once()

        if result.reason == speechsdk.ResultReason.RecognizedSpeech:
            return {"success": True, "text": result.text}
        else:
            return {"success": False, "error": "Не удалось распознать речь"}
    except Exception as e:
        return {"success": False, "error": str(e)}
