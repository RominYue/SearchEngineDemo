#-*-coding=utf8-*-

import gzip
import zlib
import base64 as b64
import chardet
from cStringIO import StringIO
from bson.binary import Binary
from collections import OrderedDict
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

KEYS = [
    ('_id','warc-trec-id'),
    ('warc_version', 'version'),
    ('warc_type', 'warc-type'),
    ('warc_warcinfo_id', 'Warc-warcinfo-id'),
    ('warc_date', 'warc-date'),
    ('warc_trec_id', 'warc-trec-id'),
    ('warc_ip_address', 'warc-ip-address'),
    ('warc_target_uri', 'warc-target-uri'),
    ('warc_record_id', 'warc-record-id'),
    ('warc_payload_digest', 'warc-payload-digest'),
    ('content_type', 'content-type'),
    ('content_length', 'content-length'),
    ('payload_type', 'warc-identified-payload-type'),
    ('warc_request_uri', 'warc-request-uri'),
    ('inlinks', 'inlinks'),
    ('outlinks', 'outlinks'),
    ('pagerank', 'pagerank'),
    ('anchor_text', 'anchor_text'),
    ('spam_score', 'spam_score'),
    ('http_header', 'http_header'),
    ('html', 'html')
]

def decode_unicode(tmp_str):
    info = chardet.detect(tmp_str)
    encoding = info['encoding']
    try:
        ret = tmp_str.decode(encoding)
    except Exception as e:
        ret = unicode(tmp_str ,errors='ignore')
    return ret

class MongoDoc(object):
    """docstring for MongoDoc"""
    def __init__(self, record):
        self.record = record

    def gen_mongo_doc(self):
        doc = OrderedDict()
        tmp = dict()
        tmp.update(self._get_warc_header())
        tmp.update(self._get_http_header_body())

        for key, value in KEYS:
            if tmp.has_key(value):
                if value == 'html':
                    doc[key] = tmp[value]
                else:
                    doc[key] = decode_unicode(tmp[value])
            else:
                doc[key] = u''
        return doc

    def _get_warc_header(self):
        warc_header = self.record.header
        return dict(warc_header.items())

    def _get_http_header_body(self):
        '''
        Returns
        -------
        Dict: {'http_header':str, 'html': gzipped html}
        '''

        payload = StringIO(self.record.payload)

        http_header, html_str = '', ''
        first, start = True, False
        for line in payload:
            if first:
                line = line.strip()
                if len(line) == 0 and not start:
                    continue
                elif len(line) == 0 and start:
                    first = False
                else:
                    start = True
                    http_header += line + '\n'
            else:
                html_str += line

        gzipped_html_str = self._compress(html_str)
        ret = OrderedDict()
        ret['http_header'] = http_header
        ret['html'] = gzipped_html_str
        return ret

    def _compress(self, html_str):
        tmp = zlib.compress(html_str)
        return Binary(tmp)

    def _decompress(self, gzipped_html_str):
        return zlib.decompress(gzipped_html_str)
