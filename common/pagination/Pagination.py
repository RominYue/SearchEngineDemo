#-*-coding: utf8-*-

from math import ceil

class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def prev(self):
        return self.page - 1

    @property
    def has_next(self):
        return self.page < self.pages

    @property
    def next(self):
        return self.page + 1

    def iter_pages(self, left_current=2, right_current=10):
        left_bound = self.page - left_current if self.page - left_current >0 else 1
        right_bound = self.page + right_current if self.page + \
        right_current <= self.pages else self.pages
        for num in xrange(left_bound, right_bound + 1):
            yield num

if __name__ == '__main__':
    a = Pagination(1, 10, 1000)
    print a.has_prev
    print a.has_next
    for x in a.iter_pages():
        print x
