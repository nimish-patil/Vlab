from django.shortcuts import render
from django.http import HttpResponse
import json
import pickle
import pandas as pd
import numpy as np
from transformers import pipeline
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from nltk.tokenize import RegexpTokenizer
from sklearn import metrics
from django.http import JsonResponse
import sys

def simulation(request):
    data = "Hello There"
    return render(request,'sentiment.html')  

def findSentiment(request):
    text = str(request.body)
    sentences = text[text.find('data')+5:-1].split('.')
    print(sentences)
    # file = open(r'C:\Users\hp\Desktop\SentimentAnalysis\sentimentAnalysis\sentimentAnalysis\model.sav', 'rb')
    # model = pickle.load(file)
    # token = RegexpTokenizer(r'[a-zA-Z0-9]+')
    # if text:
    #     cv = CountVectorizer(stop_words='english', ngram_range=(1,1), tokenizer = token.tokenize)
    #     text_counts = cv.fit_transform(sentences)
    #     x = text_counts.toarray()
    #     result = model.predict(x)
    classifier = pipeline("sentiment-analysis")
    result=classifier(sentences[0])[0]
    label = result['label']
    score = result['score']
    print(result)
    return JsonResponse({'text': sentences[0], 'score': score, 'sentiment': label})