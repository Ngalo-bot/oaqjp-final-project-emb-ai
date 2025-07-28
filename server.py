"""
server.py

This module implements a Flask web application for emotion detection
using the Watson NLP library.
"""

import json
from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    """Render the index page."""
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """Detect emotion from the user's input statement.

    Returns:
        JSON response with the emotion analysis or an error message
    """
    statement = request.args.get('textToAnalyze')

    # Call the emotion detector
    response = emotion_detector(statement)
    # Use json.loads to convert the JSON string to a dictionary
    emotion_data = json.loads(response)

    # Check for blank input or invalid emotions
    if emotion_data['dominant_emotion'] is None:
        return jsonify({"message": "Invalid text! Please try again!"})

    # Formating
    output_message = (f"For the given statement, the system response is"
    f"'anger': {emotion_data['anger']}, 'disgust': {emotion_data['disgust']},"
    f"'fear': {emotion_data['fear']}, 'joy': {emotion_data['joy']}"
    f"and 'sadness': {emotion_data['sadness']}. The dominant emotion is"
    f"{emotion_data['dominant_emotion']}.")
    return jsonify({"message": output_message})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
