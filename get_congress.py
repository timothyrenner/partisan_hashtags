#!/usr/bin python

from sunlight import congress
from csv import DictWriter
import os

leg = congress.all_legislators_in_office()

handles = [{'party': x['party'], 'twitter': x['twitter_id']} 
		   for x in leg if 'twitter_id' in x and
						   x['twitter_id'] is not None]

directory = os.getcwd()

if not os.path.exists(directory + "/data"):
	os.makedirs(directory + "/data")

with open('data/congress.csv','w') as f:
	writer = DictWriter(f, fieldnames = ['party', 'twitter'])
	writer.writeheader()
	for x in handles:
		writer.writerow(x)
