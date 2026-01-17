'''
Backend code for the emotion detector webapp
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def render_index():
    '''
    Renders the main page of the webapp
    '''
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    '''
    runs the input text through the emotion detector, returns formatted output
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze is None:
        return "No text provided for analysis"
    emotions = emotion_detector(text_to_analyze)
    # Check for server error response
    if emotions['dominant_emotion'] is None:
        return "Invalid text! Please try again!!"
    response_msg = f"For the given statement, the system response is "\
    f"'anger': {emotions['anger']}, 'disgust': {emotions['disgust']}, "\
    f"'fear': {emotions['fear']}, 'joy': {emotions['joy']} and "\
    f"'sadness': {emotions['sadness']}. The dominant emotion is "\
    f"{emotions['dominant_emotion']}."
    return response_msg

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
