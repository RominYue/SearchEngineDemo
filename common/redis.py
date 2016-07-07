#-*-coding: utf8-*-

import redis


def connection(ip, port):
    r = redis.StrictRedis(host=ip, port=port, db=0)
    return r


def add(r, query, suggestions):
    '''
    :param query: string
    :param suggestions: {sug1:score1,sugg2:score2...}
    use SortedSet to store suggestions
    '''
    r.zadd('suggestions', suggestions)


def search(r, query):
    return r.zrange('suggestions', start=0, end=10)

if __name__ == '__main__':
    pass
