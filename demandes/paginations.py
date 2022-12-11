from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class CodePouceDemandePagination(PageNumberPagination):
    page_size = 3

    def get_paginated_response(self, data):
        response = Response(data)
        response['current'] = self.page.number
        response['next'] = self.page.next_page_number() if self.page.has_next() else None
        response['previous'] = self.page.previous_page_number() if self.page.has_previous() else None
        response['total'] = self.page.paginator.num_pages
        response['items'] = self.page.paginator.count

        return response
