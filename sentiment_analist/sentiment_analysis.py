# -*- coding: utf-8 -*-

#Se importa TextBlob
from textblob import TextBlob

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import logging #libreria para el logging
import os
import sys
import time


class SentimenAnalysis(object):
	def __init__(self):
		self.logger = logging.getLogger('main')
		self.config_logging()
	
	def config_logging(self):
		self.logger.setLevel(logging.DEBUG)
		formatter = logging.Formatter(
			'%(asctime)s [%(threadName)s %(module)s %(funcName)s line:%(lineno)s] %(levelname)s: %(message)s',
			'%Y-%m-%d %H:%M:%S')

		log_file_name = 'sentiment.log'

		handler = logging.FileHandler(os.path.join('./logs', log_file_name))
		handler.setFormatter(formatter)
		handler.setLevel(logging.DEBUG)

		console = logging.StreamHandler()
		console.setFormatter(formatter)
		console.setLevel(logging.DEBUG)

		self.logger.handlers = []
		self.logger.addHandler(handler)
		self.logger.addHandler(console)
	
	def main(self):
		print("Probando sentiment analysis entre 0-1")
		texto = 'No tengo amigos'
		
		print(self.sentiment_analysis(texto))
		
	def sentiment_analysis(self, texto):
		analisis = TextBlob(texto)
		#idioma = analisis.detect_language()
		# meter libreria para faltas ortografia
		
		traduccion = analisis.translate(to='en')
		
		analyzer = SentimentIntensityAnalyzer()
		vs = analyzer.polarity_scores(traduccion)
		
		dic = {'mal': -3, 'pegar':-3, 'amenazar':-3, 'no':-3, 'amigos':-3}
		
		valor = 0
		words = texto.lower().split(' ')
		for word in words:
			if word in dic:
				if word == 'amigos':
					if 'no' in words:
						valor+= dic[word]
					continue
				valor += dic[word]


		return vs

if __name__ == '__main__':
	sentiment = SentimenAnalysis()
	sentiment.main()