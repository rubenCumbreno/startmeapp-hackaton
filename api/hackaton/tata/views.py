from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse
import json
import requests
#Se importa TextBlob
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer



def index(request):
	texto = ['hoy he tenido un mal día', 'lo que pasa es que no tengo amigos', '¿que actividades puedo realizar?', 'que guay!, me gusta',
	'mis amigos me hacen bullying']
	SA = sentiment_analysis(texto)
	dic_sa = {'neg'}

	return JsonResponse(SA, safe=False)


def sentiment_analysis(textos):
		total_analisis = []
		dic = {'mal': -3, 'pegar':-3, 'amenazar':-3, 'no':-3, 'amigos':-3}
		valor = 0
		for sentence in textos:
			analisis = TextBlob(sentence)
			traduccion = analisis.translate(to='en')
			analyzer = SentimentIntensityAnalyzer()
			vs = analyzer.polarity_scores(traduccion)
			
			'''words = sentence.lower().split(' ')
			for word in words:
				if word in dic:
					if word == 'amigos':
						if 'no' in words:
							valor+= dic[word]
						continue
					valor += dic[word]
			'''
			total_analisis.append(vs)
			print(vs)
		reduce_sa = reduce_analisis(total_analisis)
		return reduce_sa

def reduce_analisis(analisis_list):
	n_elementos = len(analisis_list)
	total_compound = 0
	for element in analisis_list:
		total_compound += element['compound']
	
	return total_compound/n_elementos