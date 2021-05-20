import re
import os
from tqdm import tqdm


os.chdir('/Volumes/jagl/курсовая/corpus_by_ending')
files = os.listdir()


# check whether the filename is adequate and the file can be used:
def check_validity(name):
    ending = re.findall('_(\w{4})\.', name)
    if ending:
        allowed = {'ж', 'м', 'д'}
        end = set(ending[0])
        if len(end-allowed) == 0:
            return True
        else:
            return False
    else:
        return False


# remove all files with inadequate names:
for f in tqdm(files):
    if not check_validity(f):
        if os.path.isfile(f):
            os.remove(f)
        else:  # Show an error
            print("Error: %s file not found" % f)


# check whether the file is big enough:
def check_size(file):
    file_stats = os.stat(file)
    size = file_stats.st_size / (1024 * 1024)
    if size < 1:
        return False
    else:
        return True


# delete the files that are too small:
for f in tqdm(files):
    if not check_size(f):
        if os.path.isfile(f):
            os.remove(f)
        else:  # Show an error
            print("Error: %s file not found" % f)
