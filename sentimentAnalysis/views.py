from django.shortcuts import render
from transformers import pipeline
from django.http import JsonResponse
import urllib.parse
import json

def home(request):
    return render(request, 'home.html')

def procedure(request):
    return render(request, 'procedure.html')

def theory(request):
    return render(request, 'theory.html')

def test(request):
    return render(request, 'test.html')

def simulation(request):
    return render(request, 'simulation.html')  

def findSentiment(request):

    byte_str = request.body
    string = byte_str.decode('utf-8')  # decode the byte string to a normal string
    data = json.loads('{"' + string.replace('=', '":"').replace('%20', ' ') + '"}')
    encoded_string = data['text']
    text = urllib.parse.unquote(encoded_string)
    sentences = text.split('?')

    average_score = 0
    classifier = pipeline("sentiment-analysis")
    print(sentences)

    for index, sentence in enumerate(sentences): 
        result=classifier(sentence)[0]
        print(result)
        if result['label']=='POSITIVE' and index==0:
            average_score = result['score']
        elif result['label']=='POSITIVE':
            average_score = (average_score+result['score'])/2
        elif result['label']=='NEGATIVE' and index==0:
            average_score = -(result['score'])
        else:
            average_score = (average_score-result['score'])/2
        print(average_score)

    if average_score>0:
        label = 'POSITIVE'
    else:
        label = 'NEGATIVE'

    score = str(abs(average_score)*100)[:5]
    print(text)
    return JsonResponse({'text': text, 'score': score, 'sentiment': label})