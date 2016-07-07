#-*-coding: utf8-*-

import sys
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf8')

from common import pysolr
from common.pysolr import Results
import requests

def test_search(solr):
    '''
    results is a iterator
    doc is a dict
    '''
    query = 'body:google buffer AND body:facebook'.decode('utf-8')
    params = {
        'rows':1000,
        'hl':'true',
        'hl.fl': 'body',
        'hl.fragsize': 10,
        'hl.snippets':3
    }
    results = solr.search(query, **params)
    #for doc in results.docs:
    #    for key in doc:
    #        print key
    #    print '==============='
        #print doc
    print len(results.docs)
    print results.hits


if __name__ == '__main__':
    solr = pysolr.Solr('http://xxx.xxx.xxx.xx:xxxx/solr/test/', timeout = 10)
    test_search(solr)
    #r = requests.get('http://xxx.xxx.xxx.xxx:xxxx/solr/test/select?indent=on&q=body:google buffer&rows=3&wt=json')
    #x = Results(r.json())
    #print type(x)
    #print x.hits
    #print len(x.docs)
    #print r.url
    #print r.headers
    #a = r.json()
    #print type(a)
    #print a

