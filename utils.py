
# Copyright (c) @kkahloots

import yaml
from datetime import datetime, timezone

def get_config():
    config = list(yaml.safe_load_all(open('running_config.yaml')))
    config = {k: v for x in config for k, v in x.items()}
    return config['config']

def logger(fn):

    def inner(*args, **kwargs):
        called_at = datetime.now(timezone.utc)
        print('{0} starting. Logged at {1}'.format(fn.__name__, called_at))
        to_execute = fn(*args, **kwargs)
        print('{0} done. Logged at {1}'.format(fn.__name__, called_at))
        return to_execute

    return inner