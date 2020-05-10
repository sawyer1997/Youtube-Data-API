from fampay_project.celery import app
from core.constants import REDIS_KEY
from core.utils import youtube_data_api
from redis.client import Redis
import logging

logger = logging.getLogger(__name__)

redis_client = Redis()

@app.task
def store_youtube_data_api():
	try:
		print('It is working!!')
		final = youtube_data_api()
		# Set final to redis
		if final:
			redis_value = str(final)	# converting value to redis value
			is_set = redis_client.set(REDIS_KEY, redis_value, ex=70)
			logger.info('Youtube API response: {} and value set to radis: {}'.format(final, is_set))
		return None
	except Exception as e:
		logger.error('Something went wrong!')


