'''
    Excuting this function will create a Flask channel
'''

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def analyzer():
    '''This code receives the text and analyze it.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    anger = response["anger"]
    disgust = response["disgust"]
    fear = response["fear"]
    joy = response["joy"]
    sadness = response["sadness"]
    dominant_emotion = response["dominant_emotion"]

    if dominant_emotion is None:
        return "Invalid text! Please try again."

    return f"For the given statement, the system response is 'anger': {anger},\
     'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}.\
      The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    '''This function is to render the index.html page.
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
