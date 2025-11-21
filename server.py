from flask import Flask ,request , render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector app")

@app.route("/emotionDetector")
def emotion_detect() :
    text_analyzer = request.args.get("textToAnalyze")
    response = emotion_detector(text_analyzer)
    if not response['dominant_emotion'] :
        return "Invalid text Please try again!."
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response["sadness"]
    dominant_emotion = response['dominant_emotion']
    return f"For the given statement, the system response is 'anger' : {anger} , 'disgust' : {disgust}, 'fear' : {fear}, 'joy' : {joy}, 'sadness' : {sadness} .\n The dominant emotion is {dominant_emotion} . "

@app.route("/")
def render_index_page() :
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

