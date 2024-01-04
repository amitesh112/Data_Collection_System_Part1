import os
import logging
import faktory
import time

# Setting the default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project1_implementation.settings')

# Basic logging configuration
logging.basicConfig(format='%(asctime)s %(levelname)-8s %(message)s',
                    level=logging.INFO,
                    datefmt='%Y-%m-%d %H:%M:%S')

def reddit_data_collection_job():
    try:
        logging.info("Starting reddit_data_collection command")
        os.system('python manage.py reddit_data_collection')
        logging.info("Finished reddit_data_collection command")

        # Introducing a delay before re-queueing
        # time.sleep(600)  # 10 minutes delay

        with faktory.connection("tcp://:fd0a59b4a5ed08a9@localhost:7419") as client:
            client.queue("reddit_data_collection_job", queue="django_jobs", reserve_for=60*10)
    except Exception as e:
        logging.error(f"Error in reddit_data_collection_job: {e}")

def chan_data_collection_job():
    try:
        logging.info("Starting 4chan_data_collection command")
        os.system('python manage.py 4chan_data_collection')
        logging.info("Finished 4chan_data_collection command")

        # Introducing a delay before re-queueing
        time.sleep(600)  # 10 minutes delay

        with faktory.connection("tcp://:fd0a59b4a5ed08a9@localhost:7419") as client:
            client.queue("chan_data_collection_job", queue="django_jobs", reserve_for=60*10)
    except Exception as e:
        logging.error(f"Error in chan_data_collection_job: {e}")

if __name__ == "__main__":
    # This will start the Reddit data collection job when the script is run
    reddit_data_collection_job()

    # This will start the 4chan data collection job when the script is run
    chan_data_collection_job()
