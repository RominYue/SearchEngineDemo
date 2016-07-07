#-*-coding: utf8-*-

import sys
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf-8')
from common import pysolr
from HtmlEntity import HtmlEntity

class SolrClient(object):
    def __init__(self, ip_string):
        self.solr = pysolr.Solr(ip_string)
        self.docs = []

    def addDoc(self, htmlEntity):
        doc = {
            'id': htmlEntity.getTrecID(),
            'title': htmlEntity.getTitle(),
            'url': htmlEntity.getUrl(),
            'url_text': htmlEntity.getUrl(),
            'domain_0': htmlEntity.getDomain()[0],
            'domain_1': htmlEntity.getDomain()[1],
            'domain_2': htmlEntity.getDomain()[2],
            'body': htmlEntity.getBody()
        }
        self.docs.append(doc)

    def addDocs(self):
        self.solr.add(self.docs, overwrite=True)
        self.docs = []

    def commit(self):
        return self.solr.commit()

    def optimize(self):
        return self.solr.optimize()

if __name__ == '__main__':
    solrClient = SolrClient('http://183.174.228.17:8283/solr/')
    print solrClient.solr
