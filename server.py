''' This is an AI-based emotion detection Flask application '''

# import required libraries
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

# instantiate flask
app = Flask("emotion detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
    runs emotion detection over it using emotion_detector()
    function. The output returned shows the emotions and their scores 
    for the provided text.
    '''

    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion_detector function and store the response
    response = emotion_detector(text_to_analyze)

    if list(response.values()) == [None for i in response]:
        return "Invalid text! Please try again!"
    return response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)

