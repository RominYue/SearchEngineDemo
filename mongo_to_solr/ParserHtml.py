#-*-coding: utf8-*-

import sys
reload(sys)
sys.path.append('..')
sys.setdefaultencoding('utf-8')

import zlib
import chardet
from bs4 import BeautifulSoup
from pymongo import MongoClient
from HtmlEntity import HtmlEntity
from common.ExtractLevelDomain import ExtractLevelDomain

def decode_unicode(tmp_str):
    info = chardet.detect(tmp_str)
    encoding = info['encoding']
    try:
        ret = tmp_str.decode(encoding)
    except Exception as e:
        ret = unicode(tmp_str ,errors='ignore')
    return ret

def transform_text(text):
    #content = ''.join([text for text in soup.body.stripped_strings])
    text = ' '.join(text.split())
    return text

class ParserHtml(object):
    """docstring for ParserHtml"""
    def __init__(self):
        pass

    def parseHtml(self, record, htmlEntity):
        trec_id = record['_id']
        url = record['warc_target_uri']
        header = record['http_header']
        zlibed_html = record['html']
        html = self._decompress(zlibed_html)
        try:
            html = html.decode('utf-8')
        except Exception as e:
            html = decode_unicode(html)

        #parse url to get domain
        domain_parser = ExtractLevelDomain()
        domain_0 = domain_parser.parse_url(url)
        domain_1 = domain_parser.parse_url_level(url,level=1)
        domain_2 = domain_parser.parse_url_level(url,level=2)

        #parse html
        soup = BeautifulSoup(html, 'lxml')
        title = soup.title.get_text() if soup.title else ""
        meta = soup.meta
        content = soup.body.get_text() if soup.body else ""
        body = transform_text(content)

        #set htmlEntity
        htmlEntity.setTrecID(trec_id)
        htmlEntity.setUrl(url)
        htmlEntity.setTitle(title)
        htmlEntity.setBody(body)
        htmlEntity.setDomain([domain_0, domain_1, domain_2])

        return htmlEntity

    def _decompress(self, zlibed_html):
        return zlib.decompress(zlibed_html)

if __name__ == '__main__':
    client = MongoClient(host='183.174.228.25',port = 27017)
    db = client.clue_web
    record = db.trec09_Category_B.find_one({"_id" : "clueweb09-en0000-00-00003"})
    htmlEntity = HtmlEntity()
    parser = ParserHtml()
    htmlEntity = parser.parseHtml(record, htmlEntity)
    print htmlEntity
