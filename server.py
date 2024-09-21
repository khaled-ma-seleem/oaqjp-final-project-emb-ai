from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("emotion detector")

@app.route("/emotionDetector")
def emo_detector():
    
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if list(response.values()) == [None for i in response]:
        return "Invalid text! Please try again!"
    
    else:
        return response

@app.route("/")
def render_index_page():

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
