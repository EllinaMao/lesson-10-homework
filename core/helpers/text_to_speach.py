"pip install azure-cognitiveservices-speech"

import azure.cognitiveservices.speech as speechsdk
from azure.core.credentials import AzureKeyCredential

import utils as u


(AZURE_URL, AZURE_KEY, AZURE_REGION) = u.get_creds()

speech_config = speechsdk.SpeechConfig(
    subscription=AZURE_KEY,
    region=AZURE_REGION,
)

voice_name = "en-US-GuyNeural"
speech_config.speech_synthesis_voice_name = voice_name

synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config)

text_to_speak = "Some text, im really terrified wow"
style = "terrified"

ssml_string = f"""
<speak version="1.0" xmlns="http://www.w3.org/2001/10/synthesis"
       xmlns:mstts="https://www.w3.org/2001/mstts" xml:lang="en-US">
    <voice name="{voice_name}">
        <mstts:express-as style="{style}">
            {text_to_speak}
        </mstts:express-as>
    </voice>
</speak>
"""

synthesizer.speak_ssml_async(ssml_string).get()

'''он тут говорит'''