#-*-coding=utf8-*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import OrderedDict


def get_query_info(query_path):
    query_dict = OrderedDict()
    with open(query_path) as f:
        for line in f:
            terms = line.split(':')
            terms = [term.strip() for term in terms]
            query_dict[terms[0]] = terms[1]
    return query_dict


def gen_save_submmit(query_results, save_path):
    '''
    line format: queryID Q0 trec_id rank score runid
    '''
    ofs = open(save_path, 'w')
    for query_id, ResultObj in query_results:
        trec_id_dict = _get_run_trec_id(ResultObj)
        for rank, trec_id in trec_id_dict.items():
            tmp_str = '%s Q0 %s %d %.2f runid\n' % (query_id, trec_id, rank, 1.0/rank)
            ofs.write(tmp_str)
    ofs.close()


def _get_run_trec_id(ResultObj):
    trec_id_dict = OrderedDict()
    cnt = 1
    for doc in ResultObj['docs']:
        trec_id_dict[cnt] = doc['id']
        cnt += 1
    return trec_id_dict


def read_eval(eval_path):
    '''
    line format: measure\tall\tnumber
    '''
    eval_result = {}
    with open(eval_path) as f:
        for line in f:
            terms = line.split('\t')
            terms = [term.strip() for term in terms]
            if len(terms) != 3:
                continue
            eval_result[terms[0]] = terms[2]
    return eval_result
