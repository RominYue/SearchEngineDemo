#coding=utf8
'''
Created on Feb 14, 2016

@author: myue
'''

import os
from logging import config

DEBUG = True
LOG_PATH = os.getcwd()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '%(levelname)s %(asctime)s %(process)d %(message)s'
        },
        'detail': {
            'format': '%(levelname)s %(asctime)s %(process)d ' +
                      '[%(module)s.%(funcName)s line:%(lineno)d] %(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'file': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_PATH + '/info.log',
        },
        'check': {
            'level': 'INFO',
            'formatter': 'simple',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': LOG_PATH + '/check_count.log',
        }
    },
    'loggers': {
        'normal': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
        'check': {
            'handlers': ['check'],
            'level': 'INFO',
            'propagate': True,
        }
    }
}

config.dictConfig(LOGGING)
