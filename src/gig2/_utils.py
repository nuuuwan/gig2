"""Utils."""

import logging
import os

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('gig2')

DIR_DATA = '/Users/nuwan.senaratna/Not.Dropbox/_CODING/data/gig2-data'


def get_table_file(space_id, time_id, attr_id):
    return os.path.join(DIR_DATA, f'{space_id}.{time_id}.{attr_id}.tsv')
