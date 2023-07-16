import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics import mean_squared_error
from pandas.plotting import scatter_matrix
import seaborn as sns
sns.set(style="white")
sns.set(style="whitegrid", color_codes=True)



# Function that get movie recommendations based on the cosine similarity score of movie genres
def genre_recommendations(title):
	global indices,cosine_sim,data
	idx = indices[title]
	sim_scores = list(enumerate(cosine_sim[idx]))
	sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
	sim_scores = sim_scores[1:21]
	print(sim_scores)
	movie_indices = [i[0] for i in sim_scores]
	print(movie_indices)
	return data.iloc[movie_indices]

def process(path,query):
	global indices,cosine_sim,data
	data = pd.read_csv('dataset.csv',usecols=['videoid','title','viewCount','commentCount','likeCount','dislikeCount'])
	data=data.fillna(0)
	print(data)
	
	print(data.head())
	names=list(data.columns)

	correlations = data.corr()
	# plot correlation matrix
	fig = plt.figure()
	fig.canvas.set_window_title('Correlation Matrix')
	ax = fig.add_subplot(111)
	cax = ax.matshow(correlations, vmin=-1, vmax=1)
	fig.colorbar(cax)
	ticks = np.arange(0,9,1)
	ax.set_xticks(ticks)
	ax.set_yticks(ticks)
	ax.set_xticklabels(names)
	ax.set_yticklabels(names)
	#fig.savefig('Correlation Matrix.png')
	    
	plt.pause(5)
	plt.show(block=False)
	plt.close() 
	#scatterplot
	scatter_matrix(data)
	    
	plt.pause(5)
	plt.show(block=False)
	plt.close()

	

	tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
	tfidf_matrix = tf.fit_transform(data['title'])
	tfidf_matrix.shape

	cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)
	cosine_sim[:4, :4]

	# Build a 1-dimensional array with movie titles
	titles = data['title']
	indices = pd.Series(data.index, index=data['title'])
	print(indices)
	print("recommendations")
	#result=genre_recommendations('Just For Laughs Gags - Best Off').head(5)
	result=genre_recommendations(query).head(5)
	return result['title']
