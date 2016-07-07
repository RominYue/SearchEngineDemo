#-*-coding: utf8-*-

import zlib
import chardet
import pymongo
import StringIO
import logging
from pymongo import MongoClient
import sys
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf-8')

from MongoInfo import MongoDoc
from warc import warc
from common import logConf


_LOGGER_NORMAL = logging.getLogger('normal')

client = MongoClient(host='xxx.xxx.xxx.xx', port=27017)
db = client.clue_web


def patch_doc(path):
    ret = []
    with open(path) as f:
        for line in f:
            terms = line.split('\t')
            terms = [term.strip() for term in terms]
            flag = terms[-1]
            if flag == 'True':
                continue
            print line.strip()
            warcfile = terms[0].split(' ')[4]
            print warcfile
            if warcfile.startswith('D'):
                process(warcfile, 'trec09_Category_B')
            elif warcfile.startswith('H'):
                process(warcfile, 'trec12_B13')


def process(warcfile, collection):
    f = warc.WARCFile(warcfile, 'rb')
    for record in f:
        mongoDoc = MongoDoc(record)
        oneDoc = mongoDoc.gen_mongo_doc()
        if oneDoc['warc_type'] == 'warcinfo':
            continue
        doc = None
        doc = db[collection].find_one({'_id': oneDoc['warc_trec_id']})
        if doc is None:
            db[collection].insert_one(oneDoc)
            tmp_str = warcfile + ' ' + oneDoc['warc_trec_id'] + ' is done.'
            _LOGGER_NORMAL.info(tmp_str)
        else:
            pass

if __name__ == '__main__':
    path = '../../test_data/check_count.log'
    patch_doc(path)
