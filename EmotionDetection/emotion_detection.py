import json
import requests

def emotion_detector(text_to_analyse):
    '''
    Takes written text as input and sends it to be analyzed for 
    emotional content
    '''
    url = 'https://sn-watson-emotion.labs.skills.network/v1/' \
          'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    input_json = { "raw_document": { "text": text_to_analyse } }
    # Call AI service
    response = requests.post(url, headers = header, json = input_json)
    # Handle error HTTP codes
    if response.status_code == 400 or response.status_code == 500:
        emotions = {}
        emotions['anger'] = None
        emotions['disgust'] = None
        emotions['fear'] = None
        emotions['joy'] = None
        emotions['sadness'] = None
        emotions['dominant_emotion'] = None
        return emotions
    # Convert response text to dictionary
    resp_dict = json.loads(response.text)
    # Extract emotions from response
    emotions = resp_dict['emotionPredictions'][0]['emotion']
    # Find emotion given the highest certainty score by the AI service
    dominant_emotion = ""
    dominant_score = 0
    for emotion, score in emotions.items():
        if score > dominant_score:
            dominant_score = score
            dominant_emotion = emotion
    emotions['dominant_emotion'] = dominant_emotion
    return emotions
