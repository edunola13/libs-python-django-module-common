# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class StandardResultsSetPagination(PageNumberPagination):
    page_size_query_param = 'page_size'

    def get_next_link(self):
        if not self.page.has_next():
            return None
        page_number = self.page.next_page_number()
        return page_number

    def get_previous_link(self):
        if not self.page.has_previous():
            return None
        page_number = self.page.previous_page_number()
        return page_number


class MongoPagination(object):
    default_page_size = 20
    page_query_param = 'page'
    page_size_query_param = 'page_size'
    max_page_size = None

    def __init__(self):
        pass

    def _positive_int(self, integer_string, strict=False, cutoff=None):
        ret = int(integer_string)
        if ret < 0 or (ret == 0 and strict):
            raise ValueError()
        if cutoff:
            return min(ret, cutoff)
        return ret

    def paginate_queryset(self, queryset, data):
        self.page = data.get('page') or 1
        self.page = self._positive_int(self.page)

        self.page_size = self.default_page_size
        if self.page_size_query_param:
            self.page_size = data.get(self.page_size_query_param) or self.page_size
            self.page_size = self._positive_int(
                self.page_size,
                True,
                self.max_page_size
            )

        self.count = queryset.clone().count()
        queryset = queryset.skip((self.page - 1) * self.page_size).limit(self.page_size)

    def paginated_response(self, data):
        return Response({
            'count': self.count,
            'next': self.page + 1 if self.count > self.page * self.page_size else None,
            'previous': self.page - 1 if self.page > 1 else None,
            'results': data
        })
