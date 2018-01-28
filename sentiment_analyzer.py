import json
import requests

def get_sentiment_analysis(text):
    try:
        result = requests.post('http://text-processing.com/api/sentiment/', data={'text': text[:45000]})
        result_json = result.json()
    except:
        print text
        pass
    return result_json