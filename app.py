
# import library 
import pandas as pd
import numpy as np 
import json
import os 


# ========================

# import slack library 
from slackbot.bot import respond_to
from slackbot.utils import download_file, create_tmp_file


# get API token 
SLACKBOT_API_TOKEN = os.environ.get("SLACKBOT_API_TOKEN")



# utility 
# ========================

def remove(path):
    """ param <path> could either be relative or absolute. """
    if os.path.isfile(path):
        os.remove(path)  # remove the file
    elif os.path.isdir(path):
        shutil.rmtree(path)  # remove dir and all contains
    else:
        raise ValueError("file {} is not a file or dir.".format(path))


# regular 
# ========================

def sample_data():
	dates = pd.date_range('20130101',periods=6)
	df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
	print (df)
	return df 



def regular_response(word):
	print (word)
	return word + '@@' 



def upload_created_file():
	df = sample_data()
	df.to_csv('sample.csv')
	command = """
	
	curl -F file=@sample.csv -F  \
	channels=C53U3HA4W,#general -F  \
	token="{}"  \
	https://slack.com/api/files.upload

	""".format(SLACKBOT_API_TOKEN)
	print (command)
	try:
		print ('start upload sample csv')
		os.system(command)
		print ('upload sample csv OK')
		remove('sample.csv')
		#os.remove('sample.csv')
	except:
		print ('upload failed')




def upload_file():
	command = """
	
	curl -F file=@/Users/yennanliu/Desktop/df_test.csv -F  \
	channels=C53U3HA4W,#general -F  \
	token="{}"  \
	https://slack.com/api/files.upload

	""".format(SLACKBOT_API_TOKEN)
	print (command)
	try:
		print ('start upload file')
		os.system(command)
		print ('upload OK')
	except:
		print ('upload failed')



# customized 
# ========================


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
	


