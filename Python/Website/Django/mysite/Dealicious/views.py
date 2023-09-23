from django.shortcuts import render
from django.http import HttpResponse 
from google import worldMap
# Create your views here.

import urllib.request 
import json

def index(response):
	if request.method == 'POST':
		city = request.POST['city']
		source = urllib.request.urlopen("https://maps.googleapis.com/maps/api/staticmap?center="+city+"&zoom=14&size=400x400&key=AIzaSyBRrTFJpK4ZqpjHwMF45OUdwwhRH0D_e5Y").read()

		list_of_data = json.loads(source)
		




