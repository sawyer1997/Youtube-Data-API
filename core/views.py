from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from django.core.paginator import Paginator
from django.conf import settings
from redis.client import Redis

from core.utils import youtube_data_api
from core.constants import REDIS_KEY, CONTENTS_IN_ONE_PAGE


import logging

logger = logging.getLogger(__name__)

redis_client = Redis()

@api_view(['GET'])
def fetch_videos(request, page):
	if request.method == 'GET':
		try:
			logger.info('Page requested: {}'.format(page))
			redis_value = redis_client.get(REDIS_KEY)
			if redis_value:
				stored_content = eval(redis_value.decode('utf-8'))
			else:
				stored_content = youtube_data_api()
				redis_client.set(REDIS_KEY, str(stored_content), ex=70)
			p = Paginator(stored_content, CONTENTS_IN_ONE_PAGE)
			content = {}
			if page > 0 and page <= p.num_pages:
				content = p.page(page).object_list
				logger.info('Content: {}'.format(content))
				return Response(content, status=status.HTTP_200_OK)
			else:
				logger.error('Page not found, total pages: {}, page requested: {}'.format(p.num_pages, page))
				return Response({'message': 'Page not found'}, status=status.HTTP_404_NOT_FOUND)
		except Exception as e:
			logger.error('Something went wrong while fetching video content!!')
			return Response({}, status=status.HTTP_404_NOT_FOUND)