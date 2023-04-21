from django.shortcuts import render
from transformers import pipeline
from django.http import JsonResponse

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
    text = str(request.body)
    sentences = text[text.find('data')+5:-1].split('.')
    print(sentences)
    classifier = pipeline("sentiment-analysis")
    result=classifier(sentences[0])[0]
    label = result['label']
    score = result['score']
    print(result)
    return JsonResponse({'text': sentences[0], 'score': score, 'sentiment': label})