''' running emotion detector server '''
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask('Emotion Detector')

''' default route '''
@app.route('/')
def render_index():
    ''' render index html '''
    return render_template('index.html')

@app.route('/emotionDetector')
def call_emotion_detector():
    ''' invoke emotion detector '''
    text_to_analyze = request.args.get('textToAnalyze')
    resp = emotion_detector(text_to_analyze)

    if resp['anger'] is not None:
        return f"For the given statement, the system response is \
        'anger': {resp['anger']}, 'disgust': {resp['disgust']}, \
        'fear': {resp['fear']}, 'joy': {resp['joy']} and 'sadness': \
        {resp['sadness']}. The dominant emotion is {resp['dominant_emotion']}."

    return "Invalid text! Please try again!"

app.run(host='0.0.0.0', port='5000')
