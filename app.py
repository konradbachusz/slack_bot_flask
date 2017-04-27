import pandas as pd
import numpy as np 




def sample_data():
	dates = pd.date_range('20130101',periods=6)
	df = pd.DataFrame(np.random.randn(6,4),index=dates,columns=list('ABCD'))
	print (df)
	return df 


def regular_response(word):
	print (word)
	return word + '@@' 