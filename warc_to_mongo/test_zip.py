#-*-coding=utf8-*-
#coding = utf8
#pymongo api: http://api.mongodb.org/python/current/tutorial.html


import zlib
from pymongo import MongoClient
from warc import warc
from MongoInfo import MongoDoc
import StringIO
import os
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


#connection
client = MongoClient(host='xxx.xxx.xxx.xx',port = 27017)
#use db
db = client.clue_web
#select collection, all oprations are in module collections


one_document = db.trec09_Category_B.find_one({"_id" : "clueweb09-en0000-00-00003"})

for key,value in one_document.items():
    if key == 'html':
        #print key
        tmp = zlib.decompress(value)
        print type(tmp)
        print tmp.decode('utf-8')
        #print '#############################'
    #else:
    #    print key
    #    print value
    #    print '===================='
