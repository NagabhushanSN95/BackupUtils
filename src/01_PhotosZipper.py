# Shree KRISHNAya Namaha
# Zips individual folders and moves them into the target directory
# Author: Nagabhushan S N
# Last Modified: 29/06/2024

import datetime
import os
import time
import traceback
from pathlib import Path

this_filepath = Path(__file__)
this_filename = this_filepath.stem


def main():
    src_directory = Path('/Volumes/HDD01/Data/Photos/Studies/07_IISc/Events/Originals')
    tgt_directory = Path('/Volumes/Expansion/Backup/Data/Photos/Studies/07_IISc/Events/Originals')
    directories_to_exclude = ['Originals']

    os.chdir(src_directory)
    event_dirpaths = sorted([event_dirpath for event_dirpath in Path('.').iterdir() if (
            (event_dirpath.is_dir()) and
            (event_dirpath.stem not in directories_to_exclude)
    )])
    for i, event_dirpath in enumerate(event_dirpaths):
        # Check if the zip file already exists
        target_zip_path = tgt_directory / (event_dirpath.stem + '.zip')
        if target_zip_path.exists():
            print(f'{i+1}/{len(event_dirpaths)}: {event_dirpath.stem} already backed up. Skipping')
            continue

        # If we are backing up originals, check if the sorted folder is already backed up. If so, no need to back up the originals
        if src_directory.stem == 'Originals':
            target_zip_path_sorted = tgt_directory.parent / target_zip_path.name
            if target_zip_path_sorted.exists():
                print(f'{i+1}/{len(event_dirpaths)}: {event_dirpath.stem} sorted files already backed up. Not backing up originals')
                continue

        target_zip_path.parent.mkdir(parents=True, exist_ok=True)
        cmd = f'zip -q -r "{target_zip_path.as_posix()}" "{event_dirpath.as_posix()}"'
        # print(cmd)
        os.system(cmd)
        print(f'{i+1}/{len(event_dirpaths)}: Backed up {event_dirpath.stem} to {target_zip_path.as_posix()}')
    return


if __name__ == '__main__':
    print('Program started at ' + datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p'))
    start_time = time.time()
    try:
        main()
        run_result = 'Program completed successfully!'
    except Exception as e:
        print(e)
        traceback.print_exc()
        run_result = 'Error: ' + str(e)
    end_time = time.time()
    print('Program ended at ' + datetime.datetime.now().strftime('%d/%m/%Y %I:%M:%S %p'))
    print('Execution time: ' + str(datetime.timedelta(seconds=end_time - start_time)))
