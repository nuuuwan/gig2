import os

from utils import tsv, www

from gig2 import _utils
from gig2._utils import log


def get_metadata():
    remote_url = os.path.join(
        'https://raw.githubusercontent.com',
        'nuuuwan/gig-data/master/census/meta.json',
    )
    return www.read_json(remote_url)


def build_census():
    for metad in get_metadata().values():
        attr_id = metad['table_id']
        remote_url = os.path.join(
            'https://raw.githubusercontent.com',
            'nuuuwan/gig-data/master/census',
            f'data.{attr_id}.tsv',
        )
        data_list = www.read_tsv(remote_url)
        table_file = _utils.get_table_file(
            'regions',
            'census2012',
            attr_id,
        )
        tsv.write(table_file, data_list)
        n_data_list = len(data_list)
        log.info(f'Wrote {n_data_list} rows to {table_file}')
