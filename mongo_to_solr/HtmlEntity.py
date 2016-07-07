#-*-coding: utf8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


class HtmlEntity(object):
    """
    title, body, url, trec_id, domain, meta

    """
    def __init__(self):
        pass

    def setBody(self, body):
        self.body = body

    def getBody(self):
        return self.body

    def setTitle(self, title):
        self.title = title

    def getTitle(self):
        return self.title

    def setUrl(self, url):
        self.url = url

    def getUrl(self):
        return self.url

    def setTrecID(self, trec_id):
        self.trec_id = trec_id

    def getTrecID(self):
        return self.trec_id

    def setMeta(self, meta):
        self.meta = meta

    def getMeta(self):
        return self.meta

    def setDomain(self, domains):
        self.domain_0 = domains[0]
        self.domain_1 = domains[1]
        self.domain_2 = domains[2]

    def getDomain(self):
        return [self.domain_0, self.domain_1, self.domain_2]

    def __str__(self):
        return "url=" + self.url + '\n' + \
               "domain_0=" + self.domain_0 + '\n' + \
               "domain_1=" + self.domain_1 + '\n' + \
               "domain_2=" + self.domain_2 + '\n' + \
               "trec_id=" + self.trec_id + '\n' + \
               "title=" + self.title + '\n' + \
               "body=" + self.body
