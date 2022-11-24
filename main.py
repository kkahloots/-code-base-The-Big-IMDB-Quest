# Copyright (c) @kkahloots

from prefect import task, flow
from datetime import datetime, timezone
from utils import get_config
from unittests import run_unittests
from scraper import scrape

@task
def start_pipeline():
    called_at = datetime.now(timezone.utc)
    print('Starting of Pipeline. Logged at {0}'.format(called_at))

@task
def end_pipeline():
    called_at = datetime.now(timezone.utc)
    print('End of Pipeline. Logged at {0}'.format(called_at))

@task
def scrape_task(config):
    base_url = config['base_url']
    top_n = config['top_n']
    top_bath = config['top_path']
    return scrape(base_url, top_bath, top_n)


@flow(name=get_config()['pipeline_name'])
def imdb_pipeline(config):
    start_pipeline()
    run_unittests()
    movie_df = scrape_task(config)
    end_pipeline()

if __name__ == '__main__':
    config = get_config()
    imdb_pipeline(config=config)
