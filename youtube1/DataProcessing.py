from apiclient.discovery import build #pip install google-api-python-client
from apiclient.errors import HttpError #pip install google-api-python-client
import pandas as pd #pip install pandas
import oauth2client.tools as oauthtools
import csv


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
# https://cloud.google.com/console

DEVELOPER_KEY = "AIzaSyDoCF6xmMXvshacwElzwRi7z3d5EgCtCY8" #"AIzaSyDocqHwYw1G1wpJ6wTL80N5cyAleFfiNvo" 
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search(words):
	youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
	search_response = youtube.search().list(
	 q=words,
	 type="video",
	 part="id,snippet",
	 maxResults=50
	).execute()

	videos = {}
	des=[]
	cat=[]
	print(search_response) 
	for search_result in search_response.get("items", []):
	 if search_result["id"]["kind"] == "youtube#video":
	    videos[search_result["id"]["videoId"]] = search_result["snippet"]["title"]
	    des.append(search_result["snippet"]["description"])
	    cat.append(words)



	#print ("Videos:\n", "\n".join(videos), "\n")
	s = ','.join(videos.keys())
	#print(s)
	videos_list_response = youtube.videos().list(
	 id=s,
	 part='id,statistics'
	).execute()
	print(videos_list_response['items'])
	res = []
	for i in videos_list_response['items']:
	 temp_res = dict(v_id = i['id'], v_title = videos[i['id']])
	 temp_res.update(i['statistics'])
	 res.append(temp_res)

	df = pd.DataFrame.from_dict(res)
	print(df)
	for n in df:
		print(n)
	df1 = pd.DataFrame({'descripteion':des})
	print (df1)		
	df2 = pd.DataFrame({'keyword':cat})
	print (df2)		
	df3 = pd.concat([df, df1,df2], axis=1)
	print(df3)
	print(df3)
	df3.to_csv('dataset.csv', mode='a',encoding='utf-8',index=False,header=False)

def process():
	with open('dataset.csv', 'w') as csvfile:
	    filewriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
	    filewriter.writerow(["commentCount","dislikeCount","favoriteCount","likeCount","videoid","title","viewCount","description","keyword"])
	csvfile.close()    
	    
	terms = ["laugh", "prank", "funny", "humorous", "ludicrous", "ridiculous", "joking","amusing", "fun", "for grins", "humor", "comical", "jolly", "hilarious",  "witty", "comic", "droll", "facetious", "jocular", "jokey", "chuckle", "goofy", "chortle","wacky"]
	#terms = ["laugh", "prank"]
	for i in terms:
		youtube_search(i)