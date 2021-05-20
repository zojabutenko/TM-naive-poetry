import os
import re


source_dir = '/Volumes/jagl/курсовая/corpus_by_meter'
os.chdir(source_dir)
files = os.listdir()

new_dir = '/Volumes/jagl/курсовая/corpus_by_ending'

for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        try:
            corpus = file.read()
            texts = corpus.split('=====')
            for t in texts:
                endings = re.findall('(\w)\n', t)
                if len(endings) > 3:
                    endings = endings[:4]
                    ending_type = ''.join(endings)
                    filename = str(f[:-10]) + ending_type
                    end_dir = new_dir + '/' + filename + '.txt'
                    with open(end_dir, 'a', encoding='utf-8') as file_write:
                        file_write.write(t + '\n=====\n')
        except UnicodeDecodeError as err:
            print(err, '\n', f)
