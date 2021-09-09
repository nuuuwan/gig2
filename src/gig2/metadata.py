import os

from utils import tsv, filex

from gig2._utils import DIR_DATA

def infer_metadata():
    metadata = []
    for file in os.listdir(DIR_DATA):
        if '.tsv' not in file:
            continue
        tokens = file.split('.')
        if len(tokens) != 4:
            continue

        space_id, time_id, attr_id = tokens[:3]
        data_file = os.path.join(DIR_DATA, file)
        data_list = tsv.read(data_file)
        n_data_list = len(data_list)
        file_size = os.path.getsize(data_file)
        metadata.append(
            dict(
                file=file,
                space_id=space_id,
                time_id=time_id,
                attr_id=attr_id,
                n_data_list=n_data_list,
                file_size=file_size,
            )
        )
    metadata_file = os.path.join(DIR_DATA, '_metadata.tsv')
    tsv.write(metadata_file, metadata)

    md_lines = ['# GIG Data']
    for metad in metadata:
        file = metad['file']
        url = os.path.join(
            'https://github.com/nuuuwan/gig2/blob/data',
            file,
        )
        md_lines.append(f'* [{file}]({url})')

    md_file = os.path.join(DIR_DATA, 'README.md')
    filex.write(md_file, '\n'.join(md_lines))
