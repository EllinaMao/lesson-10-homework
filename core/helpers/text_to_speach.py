"pip install azure-cognitiveservices-speech"

import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential

from . import utils as u

def speak_text(text_to_speak, language="en-US"):
    try:
        AZURE_URL, AZURE_KEY, AZURE_REGION = u.get_creds()
        speech_config = speechsdk.SpeechConfig(
            subscription=AZURE_KEY, region=AZURE_REGION
        )

        voice_name = None
        if language == "en-US":
            voice_name = "en-US-JennyNeural"
        if language == "uk-UA":
            voice_name = "uk-UA-PolinaNeural"
        elif language == "ru-RU":
            voice_name = "ru-RU-DariyaNeural"

        synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

        ssml_string = f"""
        <speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis" xml:lang="{language}">
            <voice name="{voice_name}">
                {text_to_speak}
            </voice>
        </speak>
        """

        result = synthesizer.speak_ssml_async(ssml_string).get()
        if result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
            return {"success": True}
        else:
            return {"success": False, "error": "Ошибка синтеза речи"}
    except Exception as e:
        return {"success": False, "error": str(e)}
