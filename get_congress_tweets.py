#!/usr/bin python

import pandas as pd
import os
from subprocess import call


directory = os.getcwd()
argstring = directory + "/bin/tweetshovel --verbose " +\
		    "--timeline %s --auth twitter_auth.json  " +\
			"| jq --raw-output '.[] | " +\
			"[[.user.screen_name], [.created_at] , " +\
			 "[.entities.hashtags | .[].text]] | " +\
			"combinations | join(\",\")' > %s_hashtags.csv"

if not os.path.exists(directory + "/hashtags"):
	os.makedirs(directory + "/hashtags")

congress = pd.read_csv('congress.csv')

for sname in congress.twitter:
	call(argstring % (sname.lower(), directory + "/hashtags/" + sname.lower()), 
		 shell=True)
