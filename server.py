''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
# Import Flask, render_template, request from the flask pramework package : TODO
from flask import Flask, render_template, request
import json

# Import the sentiment_analyzer function from the package created: 
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

#Initiate the flask app : 
app = Flask(__name__)

@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text = request.args['textToAnalyze']
    sentiment = sentiment_analyzer(text)

    label = sentiment['label']
    score = sentiment['score']

    print('label is ', label)
    print('score is ', score)

    if (label is not None) and (score is not None):
        label = label.split('_')[1]
        return f'The given text has been identified as {label} with a confidence score of {score}'

    return "Invalid input! try again"
    

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000'''
    app.run(debug=True)
