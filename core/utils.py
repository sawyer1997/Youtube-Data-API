from core.constants import PREDEFINED_SEARCH_QUERY, API_KEY
from apiclient.discovery import build

import logging
logger = logging.getLogger(__name__)

def youtube_data_api():
	try:
		youtube = build('youtube', 'v3', developerKey=API_KEY)
		request = youtube.search().list(part='snippet', 
										q=PREDEFINED_SEARCH_QUERY,
										type='video',
										order='date',
										maxResults=50)
		response = request.execute()
		final = list()
		for item in response['items']:
			content = dict()
			if item.get('snippet'):
				item_snippet = item.get('snippet')
				if item_snippet.get('publishedAt'):
					content['publishedAt'] = item_snippet['publishedAt']
				if item_snippet.get('title'):
					content['title'] = item_snippet['title']
				if item_snippet.get('description'):
					content['description'] = item_snippet['description']
				if item_snippet.get('thumbnails') and item_snippet['thumbnails'].get('default') and item_snippet['thumbnails']['default'].get('url'):
					content['thumbnailURL'] = item_snippet['thumbnails']['default']['url']
				final.append(content)
		return final
	except Exception as e:
		logger.error('Youtube API not working!!')
		return []