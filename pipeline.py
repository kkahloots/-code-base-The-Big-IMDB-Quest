# Copyright (c) @kkahloots

from prefect import task, flow
from datetime import datetime, timezone
from utils import get_config
from unittests import run_unittests

@task
def start_pipeline():
    called_at = datetime.now(timezone.utc)
    print('Starting of Pipeline. Logged at {0}'.format(called_at))

@task
def end_pipeline():
    called_at = datetime.now(timezone.utc)
    print('End of Pipeline. Logged at {0}'.format(called_at))

@flow(name=get_config()['pipeline_name'])
def imdb_pipeline():
    start_pipeline()
    run_unittests()
    end_pipeline()

if __name__ == '__main__':
    imdb_pipeline()
