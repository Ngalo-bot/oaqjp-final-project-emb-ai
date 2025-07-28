import requests
import json

def emotion_detector(text_to_analyze):
    if not text_to_analyze.strip():  
        return json.dumps( {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        })

    # Define the URL and headers for the POST request
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }

    # Create the input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Send a POST request to the EmotionPredict function
    response = requests.post(url, headers=headers, json=input_json)
    

    # Check for successful response
    if response.status_code == 200:
        emotions = response.json().get('emotionPredictions', [])
        if emotions:          
           
            scores = emotions[0]['emotion']
            # Find the dominant emotion
            dominant_emotion = max(scores, key=scores.get)
            # Create formatted output
            output = {
                'anger': scores['anger'],
                'disgust': scores['disgust'],
                'fear': scores['fear'],
                'joy': scores['joy'],
                'sadness': scores['sadness'],
                'dominant_emotion': dominant_emotion
            }
            return json.dumps(output) 
    else:
        return f"Error: {response.status_code}, {response.text}"