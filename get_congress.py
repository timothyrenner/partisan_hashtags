from sunlight import congress
from csv import DictWriter
import os

leg = congress.all_legislators_in_office()

congress_names = [{'party': x['party'], 
				   'twitter': x['twitter_id'].lower(),
				   'name': "{} {} ({})".format(x['first_name'],
				   							   x['last_name'],
											   x['state'])}
		   for x in leg if 'twitter_id' in x and
						   x['twitter_id'] is not None]

directory = os.getcwd()

if not os.path.exists(directory + "/data"):
	os.makedirs(directory + "/data")

with open('data/congress.csv','w') as f:
	writer = DictWriter(f, fieldnames = ['party', 'twitter', 'name'])
	writer.writeheader()
	for x in congress_names:
		writer.writerow(x)
