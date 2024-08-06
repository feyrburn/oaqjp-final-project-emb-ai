import requests, json

URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

def emotion_detector(text_to_analyze):
    response = requests.request(
        method = 'POST',
        url = URL,
        headers = HEADERS,
        json = { "raw_document": { "text": text_to_analyze } }
    )

    response_dict = json.loads(response.text)
    emotion_dict = response_dict['emotionPredictions'][0]['emotion']

    dominant_score = 0
    dominant_emotion = ''
    for emotion in emotion_dict.keys():
        if emotion_dict[emotion] > dominant_score:
            dominant_score = emotion_dict[emotion]
            dominant_emotion = emotion 

    final_response = {
        'anger': emotion_dict['anger'],
        'disgust': emotion_dict['disgust'],
        'fear': emotion_dict['fear'],
        'joy': emotion_dict['joy'],
        'sadness': emotion_dict['sadness'],
        'dominant_emotion': dominant_emotion
        }

    return final_response