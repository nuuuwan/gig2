import os

from utils import tsv, www

from gig2 import _utils
from gig2._utils import log


def build_elections():
    for election_type in ['presidential']:
        for year in [1982, 1988, 1994, 1999, 2005, 2010, 2015, 2019]:
            remote_url = os.path.join(
                'https://raw.githubusercontent.com',
                'nuuuwan/elections_lk/data',
                f'elections_lk.{election_type}.{year}.json',
            )
            data_list = www.read_json(remote_url)
            table = []
            for data in data_list:
                row = {}
                row['pd_id'] = 'EC-%s' % (data['pd_code'])
                row['result_ut'] = data['timestamp']
                row['valid'] = data['summary']['valid']
                row['rejected'] = data['summary']['rejected']
                row['polled'] = data['summary']['polled']
                row['electors'] = data['summary']['electors']

                for for_party in data['by_party']:
                    row[for_party['party_code']] = for_party['votes']
                table.append(row)

            table_file = _utils.get_table_file(
                'pd',
                f'{year}_election_{election_type}',
                'result',
            )
            tsv.write(table_file, table)
            n_data_list = len(data_list)
            log.info(f'Wrote {n_data_list} rows to {table_file}')
