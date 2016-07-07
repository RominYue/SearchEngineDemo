#-*-coding=utf8-*-
#coding = utf8
#pymongo api: http://api.mongodb.org/python/current/tutorial.html

import StringIO
import glob
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def stats_all_file(dirname):
    stats = {}
    filelist = glob.glob(dirname + '*.txt')
    for filename in filelist:
        with open(filename) as f:
            for line in f:
                terms = line.split('\t')
                terms = [term.strip() for term in terms]
                if len(terms) != 2:
                    continue
                warc_file = terms[0][terms[0].find('.')+1:]
                #in windows
                warc_file = warc_file.replace('/','\\')
                count = int(terms[1])
                stats[warc_file] = count
    return stats

def get_doc_num(process_filename, dirname):
    stats = stats_all_file(dirname) 
    for key,value in stats.items():
        if process_filename.endswith(key):
            return value
    return 0

if __name__ == '__main__':
    dir = 'D:\\users\\yueming_shuo\\record_count\\'
    stats_all_file(dir)
