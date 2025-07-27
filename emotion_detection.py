import requests

def emotion_detector(text_to_analyze):
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
        return response.json().get('text')  # Return the 'text' attribute from the response
    else:
        return f"Error: {response.status_code}, {response.text}"