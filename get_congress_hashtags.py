from datetime import datetime, date
import pandas as pd
from glob import glob

LAST_WEEK = date(2016,05,07)

to_dt = lambda x: datetime.strptime(x, "%a %b %d %H:%M:%S +0000 %Y")

# This function reads a file, builds a data frame, does some formatting,
# and filters all hashtags more than one week old. It's in its own function
# because we have to use statements to properly transform the data.
def trim_and_format_hashtags(filename):
	tag_frame =\
		pd.read_csv(filename, names=['name', 'time', 'tag'], header=None)
	
	# First format the frame.
	tag_frame['time'] = tag_frame['time'].map(to_dt)
	tag_frame['name'] = tag_frame['name'].map(lambda x: x.lower())
	tag_frame['tag'] = tag_frame['tag'].map(lambda x: x.lower())

	# Now get the dates more than one week old. I'm going to cheat here
	# and hard code the date.
	return tag_frame[tag_frame.time >= LAST_WEEK]
	

# Get all of the hashtag files in the 'hashtags/' directory.
hashtag_files = glob('hashtags/*.csv')

last_week_hashtags =\
	pd.concat([trim_and_format_hashtags(f) for f in hashtag_files])

last_week_hashtags.to_csv('congress_last_week_tags.csv', index=False)
