import json
import requests

def get_sentiment_analysis(text):
    result = requests.post('http://text-processing.com/api/sentiment/', data = {'text': text})
    return result.json()