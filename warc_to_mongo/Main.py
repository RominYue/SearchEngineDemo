#-*-coding=utf8-*-
#coding = utf8
#pymongo api: http://api.mongodb.org/python/current/tutorial.html

import pymongo
from pymongo import MongoClient
import StringIO
import logging
import os
import sys
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf-8')
from test_count import get_doc_num
from common import logConf
from MongoInfo import MongoDoc
from warc import warc

_LOGGER_NORMAL = logging.getLogger('normal')
_LOGGER_CHECK = logging.getLogger('check')

#connection
client = MongoClient(host='xxx.xxx.xxx.xx',port = 27017)
#use db
db = client.clue_web
#select collection, all oprations are in module collections

CHECK_DIRNAME = 'D:\\users\\yueming_shuo\\record_count\\'

def _print(dict_info):
    for k,v in dict_info.items():
        print type(k), type(v)

def get_file_list(root_dir):
    filelist = []
    for root, dirs, files in os.walk(root_dir):
        for filename in files:
            tmp = os.path.join(root, filename)
            if tmp.endswith('.warc.gz'):
                filelist.append(tmp)
    return filelist

def insert_one_file(filename, collection):
    doc_cnt = 0
    f = warc.WARCFile(filename, 'rb')
    for record in f:
        mongoDoc = MongoDoc(record)
        oneDoc = mongoDoc.gen_mongo_doc()
        if oneDoc['warc_type'] == 'warcinfo':
            continue
        db[collection].insert_one(oneDoc)
        doc_cnt += 1
        tmp_str = filename + ' ' + oneDoc['warc_trec_id'] + ' is done.'
        _LOGGER_NORMAL.info(tmp_str)

    #check doc_count is the same
    true_cnt = get_doc_num(filename,CHECK_DIRNAME)
    tmp_str = filename + '\t' + str(true_cnt) + '\t' + str(doc_cnt) + '\t' + str(true_cnt == doc_cnt)
    _LOGGER_CHECK.info(tmp_str)

def process(root_dir, collection):
        db[collection].create_index([("warc_trec_id", pymongo.ASCENDING)])
        print root_dir
        filelist = get_file_list(root_dir)
        for filename in filelist:
            print filename
            insert_one_file(filename, collection)

if __name__ == '__main__':
    ROOT_DIR = ['D:\\TREC_2009_A\\ClueWeb09_English_1','H:\\']
    process(ROOT_DIR[0], 'trec09_Category_B')
    process(ROOT_DIR[1], 'trec12_B13')

