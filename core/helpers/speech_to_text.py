"pip install azure-cognitiveservices-speech"

import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential

import utils as u


(AZURE_URL, AZURE_KEY, AZURE_REGION) = u.get_creds()

speech_config = speechsdk.SpeechConfig(
    subscription=AZURE_KEY,
    region=AZURE_REGION,
    # speech_recognition_language="uk-UA"
    speech_recognition_language="ru-ru"
)

recodnizer = speechsdk.SpeechRecognizer(speech_config= speech_config)
result = recodnizer.recognize_once()

print("Text: ", result.text)

"""
Text:  В общем, я що так говорив, я просто хочу вибити як ти робиш чи можеш встановити мене, розповісти про це дуже дякую.


Text:  В общем, расскажи мне, чтонибудь я хочу узнать, что ты думаешь, я хочу узнать, что ты говоришь и читаешь ли ты мой микрофон раз раз.
"""
