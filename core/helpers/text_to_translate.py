import azure.cognitiveservices.speech as speechsdk
import utils as u

AZURE_URL, AZURE_KEY, AZURE_REGION = u.get_creds()

speech_config = speechsdk.translation.SpeechTranslationConfig(
    subscription=AZURE_KEY,
    region=AZURE_REGION,
)

# speech_config.add_target_language("fr-CA")
speech_config.add_target_language("en-US")
speech_config.speech_recognition_language = "uk-UA"

audio_config = speechsdk.audio.AudioConfig(use_default_microphone=True)
recognizer = speechsdk.translation.TranslationRecognizer(
    translation_config=speech_config, audio_config=audio_config
)

result = recognizer.recognize_once()

print("Translation", result)

"""
(.venv) PS D:\lessons\cloud\lessons py teacher\pv_412_411_azure\lesson10_congnitive_services> py text_to_translate.py
Translation TranslationRecognitionResult(result_id=bb7441a7b40f41229b9828036de5740c, translations={'fr-CA': 'Je ne dis rien, ils me traduisent en français lyalyan.'}, reason=ResultReason.TranslatedSpeech)
(.venv) PS D:\lessons\cloud\lessons py teacher\pv_412_411_azure\lesson10_congnitive_services> 

"""
"""
  (.venv) PS D:\lessons\cloud\lessons py teacher\pv_412_411_azure\lesson10_congnitive_services> py text_to_translate.py
Translation TranslationRecognitionResult(result_id=14cfc5a8ee0c4b6a9ecc99ac2f8f5bd8, translations={'en-US': 'Of course, you tell me you too.'}, reason=ResultReason.TranslatedSpeech)
"""
