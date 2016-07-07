#-*-coding: utf8-*-

import sys
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf-8')

import logging
import pymongo
from pymongo import MongoClient
import  multiprocessing
import time
from HtmlEntity import HtmlEntity
from ParserHtml import ParserHtml
from SolrClient import SolrClient
from common import logConf

_LOGGER_ = logging.getLogger('normal')

#connection
client = MongoClient(host='xxx.xxx.xxx.xx',port = 27017)
#use db
db = client.clue_web
#collection: trec09_Category_B, trec12_B13
MCPU = 18
BATCH_NUM = 10000

def process_one(record_list, coll):
    url_solr = 'http://xxx.xxx.xxx.xx:xxxx/solr/%s/'% coll
    solrClient = SolrClient(url_solr)

    for record in record_list:
        htmlEntity = HtmlEntity()
        parser = ParserHtml()
        htmlEntity = parser.parseHtml(record, htmlEntity)
        solrClient.addDoc(htmlEntity)
    solrClient.addDocs()
    last_id = record_list[-1]['_id']
    _LOGGER_.info(last_id + ' is Done!')
    del record_list

def batch_index(coll,batch_num):
    pool = multiprocessing.Pool(processes=MCPU)
    #index
    cnt, total, pre = 0, 0, 0
    cache = []
    for record in db[coll].find(no_cursor_timeout=True).sort('_id', pymongo.ASCENDING):
        if record['_id'] <= 'clueweb09-en0002-97-31364':
            pre += 1
            print pre
            continue

        cnt += 1
        cache.append(record)
        if cnt == batch_num:
            process_count = len(pool._cache)
            print process_count, MCPU
            while process_count == MCPU:
                time.sleep(5)
                process_count = len(pool._cache)

            record_list = cache
            cache = []
            cnt = 0
            pool.apply_async(process_one, (record_list, coll))
    pool.close()
    pool.join()

if __name__ == '__main__':
    batch_index("trec09_Category_B", BATCH_NUM)
    #batch_index("trec12_B13", 5000)
