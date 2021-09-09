import os

from utils import tsv, www

from gig2._utils import log

DIR_DATA = '/tmp/gig2'


def init():
    if not os.path.exists(DIR_DATA):
        os.mkdir(DIR_DATA)


def get_table_file(attr_id, time_id, space_id):
    return os.path.join(DIR_DATA, f'{attr_id}.{time_id}.{space_id}.tsv')


def build():
    for region_type in [
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
        table_file = get_table_file(
            'basic',
            'latest',
            region_type,
        )
        tsv.write(table_file, data_list)
        n_data_list = len(data_list)
        log.info(f'Wrote {n_data_list} rows to {table_file}')


if __name__ == '__main__':
    init()
    build()
