import faktory

with faktory.connection("tcp://:fd0a59b4a5ed08a9@localhost:7419") as client:
    client.queue("reddit_data_collection_job", queue="django_jobs", reserve_for=60*10)
    client.queue("chan_data_collection_job", queue="django_jobs", reserve_for=60*10)
