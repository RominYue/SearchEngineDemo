#-*-coding: utf8-*-

import json
import sys
import random
import re
import os
sys.path.append('..')
from collections import OrderedDict

from common import bottle
from common.bottle import route, run, template, view, static_file, redirect
from common.bottle import request, response, HTTPResponse
from common.pagination.Pagination import Pagination
from common.suggestion import suggest
from common.pysolr import Results, Solr
from common.evaluation import evaluate
from common.spellcheck import spellcheck
from common.utils import exe_cmd, results_for_page, ads_for_page, parse_response
from conf.conf import EVAL_EXE, RUN_FILE_PATH, RESULT_PATH, trec_dict, baseline
from conf.conf import SOLR_URL, solr_core, solr_query_params
from conf.conf import PER_PAGE, TOTAL, AD_NUM, RUN_IP, RUN_PORT, SUGGEST_DICT
from conf.conf import WORD_PATH, BAG_OF_WORDS, SPELLCHECK_PARAM

searchType = "Collection"

trec_eval_results = OrderedDict()

tree = suggest.build(SUGGEST_DICT, is_case_sensitive=False)

wordSet, bagOfword, parameter = spellcheck.init(WORD_PATH, BAG_OF_WORDS, SPELLCHECK_PARAM)

@route('/')
@route('/home')
def home():
    return template('home.ftl')


@route('/index')
def index():
    args = request.query.decode("utf-8")
    global searchType
    if args.searchType != "":
        searchType = args.searchType
        print searchType
    return template('index.ftl', type=searchType)


@route('/query', method='POST')
def handle_query():
    args = request.forms.decode("utf-8")
    if args.query == '':
        redirect('/index')
    else:
        global searchType
        if searchType == 'Collection':
            searchType = 'Trec09'
        print searchType
        redirect('/result?searchType=%s&page=%d&query=%s' %
                 (searchType, 1, args.query))


@route('/result')
def handle_index(page=1):
    args = request.query.decode("utf-8")
    page = int(args.page)
    searchType = args.searchType
    query = args.query

    # search
    solr = Solr(SOLR_URL + '/' + solr_core[searchType] + '/')
    start = (page - 1) * PER_PAGE
    solr_query_params = {
        'start':start,
        'rows':10,
        'hl': 'true',
        'hl.fl': 'body',
        'hl.fragsize': 100,
        'hl.snippets': 3,
        'df': 'text'
    }
    responseObj = solr.search(query, **solr_query_params)
    ResultObj = parse_response(responseObj)
    resultNum = ResultObj['hits']
    print resultNum
    if resultNum == 0:
        return "No match Docs find! What's a pity"
    resultNum = resultNum if resultNum < TOTAL else TOTAL
    paginator = Pagination(page, PER_PAGE, resultNum)
    # result
    results = results_for_page(ResultObj, page, PER_PAGE, resultNum)
    # ad
    if resultNum < 2:
        ads = ads_for_page(ResultObj, 1)
    else:
        ads = ads_for_page(ResultObj, AD_NUM)

    #spellcheck
    spell_flag = True
    query_right = spellcheck.spellCorret(query, wordSet, bagOfword, parameter)
    if len(query_right) == 0:
        spell_flag = False

    template_params = {
        'query': query,
        'results': results,
        'ads': ads,
        'paginator': paginator,
        'resultNum': resultNum,
        'searchType': searchType,
        'spellFlag': spell_flag,
        'query_right': query_right
    }
    return template('result.ftl', **template_params)


@route('/suggest')
def handle_query():
    args = request.query.decode("utf-8")
    print args.keyword
    if len(args.keyword) == 0:
        return
    results = suggest.search(tree, args.keyword, limit=10)
    if len(results) == 0:
        return
    ret = [{'value': x[0]} for x in results]
    data = json.dumps(ret)
    return HTTPResponse(data, mimetype='application/json')


@route('/syseval')
def system_eval():
    global trec_eval_results,baseline
    baseline = OrderedDict(baseline)
    if len(trec_eval_results) != 0:
        template_params = {
            'trec_eval_results': trec_eval_results,
            'baseline': baseline
        }
        return template('syseval_result.ftl', **template_params)

    trec_list = ['Trec14', 'Trec09']
    R = lambda x:int(filter(str.isdigit,x))
    for trec in trec_list:
        qrels = trec_dict[trec]['qrels.adhoc']
        query_dict = evaluate.get_query_info(trec_dict[trec]['queries'])
        print 'query len %d' % len(query_dict)
        core = 'Trec09' if R(trec) < 12 else 'Trec12'
        solr = Solr(SOLR_URL + '/' + solr_core[core] + '/', timeout=100)
        results = []
        for query_id, query in query_dict.items():
            responseObj = solr.search(query, **solr_query_params)
            ResultObj = parse_response(responseObj)
            results.append([query_id, ResultObj])
        # gen submit and save
        evaluate.gen_save_submmit(results, RUN_FILE_PATH)
        # eval by eval_program
        cmd = EVAL_EXE + ' -m all_trec -M 1000 ' + qrels + ' ' + RUN_FILE_PATH + ' > ' + RESULT_PATH
        exe_cmd(cmd)
        # read eval result and display
        eval_results = evaluate.read_eval(RESULT_PATH)
        trec_eval_results[trec] = eval_results
        print trec + ' is Done!'

    template_params = {
        'trec_eval_results': trec_eval_results,
        'baseline': baseline
    }
    return template('syseval_result.ftl', **template_params)


@route('/restful/<trec>/<query>', method='GET')
def get_restful_results(trec="Trec09", query=""):
    pass


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='static')

if __name__ == '__main__':
    run(host=RUN_IP, port=RUN_PORT, debug=True, reloader=True)
    #run(server='gunicorn', host=RUN_IP, port=RUN_PORT, workers=4, worker_class='gevent', debug=False, reloader=False)
    #run(server='cherrypy', host=RUN_IP, port=RUN_PORT, debug=False, reloader=False)

#app = bottle.default_app()
