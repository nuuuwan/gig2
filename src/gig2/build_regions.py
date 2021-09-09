import os

from utils import tsv, www

from gig2 import _utils
from gig2._utils import log


def build_regions():
    for region_type in [
        'country',
        'province',
        'district',
        'dsd',
        'gnd',
        'pd',
        'ed',
        'moh',
        'lg',
    ]:
        remote_url = os.path.join(
            'https://raw.githubusercontent.com',
            'nuuuwan/gig-data/master',
            f'{region_type}.tsv',
        )
        data_list = www.read_tsv(remote_url)
        table_file = _utils.get_table_file(
            region_type,
            'latest',
            'basic',
        )
        tsv.write(table_file, data_list)
        n_data_list = len(data_list)
        log.info(f'Wrote {n_data_list} rows to {table_file}')
