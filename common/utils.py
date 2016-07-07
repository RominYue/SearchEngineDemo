#-*-coding: utf8-*-
import os
import sys
import random


def exe_cmd(cmd):
    ret = os.system(cmd)
    if ret != 0:
        sys.exit(1)


def parse_response(responseObj):
    '''Parse raw response object pysolr.Results
    '''
    ResultObj = {}
    ResultObj['docs'] = responseObj.docs
    ResultObj['highlighting'] = responseObj.highlighting
    ResultObj['qtime'] = responseObj.qtime
    ResultObj['hits'] = responseObj.hits
    return ResultObj


def results_for_page(ResultObj, page, per_page, total_count):
    '''generate display results for each page
    Parameters
    ----------
    :param ResultObj: dict from response object
    :page: int, page_num
    :per_page: int, per_page_num
    :total_count: int, num of total results

    Returns
    -------
    :results: list of docs for each page
    '''
    start = (page - 1) * per_page
    end = start + per_page - 1 if start + per_page - 1 <= total_count else total_count
    rows = end - start + 1
    docs = ResultObj['docs']
    highlights = ResultObj['highlighting']

    results = docs[:rows]
    for doc in results:
        tmp_str = '. '.join(highlights[doc['id']]['body']) + '...'
        tmp_str = tmp_str.replace('<em>', '<font color="red">')
        tmp_str = tmp_str.replace('</em>', '</font>')
        doc['highlighting'] = tmp_str
        doc['qtime'] = ResultObj['qtime']
        doc['hits'] = ResultObj['hits']
    return results


def ads_for_page(ResultObj, ad_num):
    ads = []
    docs = ResultObj['docs']
    highlights = ResultObj['highlighting']
    cnt, docSet = 0, set()
    while cnt < ad_num:
        doc = random.choice(docs)
        index = docs.index(doc)
        if index in docSet:
            continue
        docSet.add(index)
        tmp_str = '. '.join(highlights[doc['id']]['body']) + '...'
        tmp_str = tmp_str.replace('<em>', '<font color="red">')
        tmp_str = tmp_str.replace('</em>', '</font>')
        if tmp_str.find('<a>') != -1 or tmp_str.find('href') != -1:
            continue
        doc['highlighting'] = tmp_str
        ads.append(doc)
        cnt += 1
    return ads
