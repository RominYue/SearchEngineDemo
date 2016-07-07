#-*-coding: utf8-*-
import os

ROOT_PATH = os.path.abspath('../')

############## search ####################
# This part stands for search config
# Most relevant with solr
##########################################

SOLR_URL = 'http://xxx.xxx.xxx.xx:xxxx/solr'

solr_core = {
    'Trec09': 'trec09_Category_B_replica',
    'Trec12': 'trec12_B13_replica'
}

solr_query_params = {
    'rows': 1000,
    'df':'text'
}

############## WebApp #####################
# This part stands for webapp config
###########################################

# Pagination
PER_PAGE = 10
TOTAL = 1000
AD_NUM = 2

# RUN IP/PORT
RUN_IP = 'xxx.xxx.xxx.xx'
RUN_PORT = 8285

############# Evaluation ##################
# This part stands for Evaluation part
###########################################

# evaluate conf
EVAL_EXE = ROOT_PATH + '/data/trec_eval/trec_eval'
RUN_FILE_PATH = ROOT_PATH + '/data/submit/tmpfile'
RESULT_PATH = ROOT_PATH + '/data/evaluation/tmpresult'

trec_dict = {
    'Trec09': {
        'qrels.adhoc': ROOT_PATH + '/data/trec09/qrels.adhoc',
        'queries': ROOT_PATH + '/data/trec09/web2009.topics'
    },
    'Trec10': {
        'qrels.adhoc': ROOT_PATH + '/data/trec10/qrels.adhoc',
        'queries': ROOT_PATH + '/data/trec10/web2010.topics'
    },
    'Trec11': {
        'qrels.adhoc': ROOT_PATH + '/data/trec11/qrels.adhoc',
        'queries': ROOT_PATH + '/data/trec11/web2011.topics'
    },
    'Trec12': {
        'qrels.adhoc': ROOT_PATH + '/data/trec12/qrels.adhoc',
        'queries': ROOT_PATH + '/data/trec12/web2012.topics'
    },
    'Trec13': {
        'qrels.adhoc': ROOT_PATH + '/data/trec13/qrels.adhoc',
        'queries': ROOT_PATH + '/data/trec13/web2013.topics'
    },
    'Trec14': {
        'qrels.adhoc': ROOT_PATH + '/data/trec14/qrels.adhoc',
        'queries': ROOT_PATH + '/data/trec14/web2014.topics'
    }
}

baseline = {
    'Trec09': {
        'MAP': '0.043',
        'P@5': '0.346',
        'P@10': '0.40',
        'P@20': '0.41',
        'ERR@20': 'NULL',
        'nDCG@20': 'NULL'
    },
    'Trec10': {
        'MAP': '0.133',
        'P@5': 'NULL',
        'P@10': 'NULL',
        'P@20': '0.443',
        'ERR@20': '0.134',
        'nDCG@20': '0.260'
    },
    'Trec11': {
        'MAP': '0.110',
        'P@5': 'NULL',
        'P@10':'NULL',
        'P@20':'0.298',
        'ERR@20': '0.131',
        'nDCG@20': '0.233'
    },
    'Trec12': {
        'MAP': '0.131',
        'P@5': 'NULL',
        'P@10':'NULL',
        'P@20':'0.405',
        'ERR@20': '0.299',
        'nDCG@20':'0.214'
    },
    'Trec13': {
        'MAP': 'NULL',
        'P@5': 'NULL',
        'P@10':'NULL',
        'P@20':'NULL',
        'ERR@20': '0.184',
        'nDCG@20': '0.310'
    },
    'Trec14': {
        'MAP': 'NULL',
        'P@5': 'NULL',
        'P@10':'NULL',
        'P@20':'NULL',
        'ERR@20': '0.233',
        'nDCG@20': '0.325'
    }
}
########### Suggestion ######################
# Suggestion Config
#############################################

#SUGGEST_DICT = ROOT_PATH + '/data/suggest/data.txt'
SUGGEST_DICT = ROOT_PATH + '/data/suggest/sample_suggest.dict'


#############################################
# Spellcheck
#############################################

WORD_PATH = ROOT_PATH + '/data/spellcheck/word.txt'
BAG_OF_WORDS = ROOT_PATH + '/data/spellcheck/bagOfword.txt'
SPELLCHECK_PARAM = ROOT_PATH + '/data/spellcheck/parameter.txt'
