from celery import Celery
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def make_celery(app):
    celery = Celery(
        app.import_name,
        broker=os.getenv('CELERY_BROKER_URL'),
        backend=os.getenv('CELERY_RESULT_BACKEND')
    )
    
    celery.conf.update(app.config)
    celery.autodiscover_tasks(['app'])  # Ensure the app module is discovered
    return celery