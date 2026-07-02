import requests
import uuid
from . import utils as u

def translate_text(text, target_lang="en"):
    try:
        AZURE_URL, AZURE_KEY, AZURE_REGION = u.get_creds()

        endpoint = "https://api.cognitive.microsofttranslator.com/translate"
        params = {"api-version": "3.0", "to": target_lang}
        headers = {
            "Ocp-Apim-Subscription-Key": AZURE_KEY,
            "Ocp-Apim-Subscription-Region": AZURE_REGION,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }
        body = [{"text": text}]
        response = requests.post(endpoint, params=params, headers=headers, json=body)

        if response.status_code == 200:
            result = response.json()
            return {
                "success": True,
                "translated_text": result[0]["translations"][0]["text"],
            }
        else:
            return {"success": False, "error": f"Ошибка перевода: {response.text}"}
    except Exception as e:
        return {"success": False, "error": str(e)}
