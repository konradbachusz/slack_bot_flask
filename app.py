import pandas as pd
import numpy as np 
import json
import os 



def sample_data():
	dates = pd.date_range('20130101',periods=6)
	df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
	print (df)
	return df 


def regular_response(word):
	print (word)
	return word + '@@' 



def spotify_album(artist):
	# make sure artist name feat spotify API query form 
	artist = artist.replace (" ", "+")
	print (artist)
	url="https://api.spotify.com/v1/search?q=${}&type=artist".format(artist)

	command = """ 
	API_ARTIST_URL=$(curl -s "{}" | jq -r '.artists.items[0].href') 
	curl -s "$API_ARTIST_URL/top-tracks?country=US" > spotify_data.json
	""".format(url)
	print (command)
	os.system(command)
	album = ''
	try:
		data_spotify = json.loads(open('spotify_data.json').read())
		for k in range(0,len(data_spotify['tracks'])): 
		    print (data_spotify['tracks'][k]['name'])
		    album += data_spotify['tracks'][k]['name'] + "\n\n"
	except:
		album = 'no feat artist, return null data'
		print (album)
	# remove intermediate json 	
	os.system('rm spotify_data.json')
	return album
	


