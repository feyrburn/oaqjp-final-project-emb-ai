import requests

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    response = requests.request(
        method = 'POST',
        url = URL,
        headers = HEADERS,
        json = { "raw_document": { "text": text_to_analyze } }
    )

    return response.text