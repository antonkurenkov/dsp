
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class ReactAdminPagination(PageNumberPagination):
    page_query_param = "page"
    page_size_query_param = "perPage"

    def get_paginated_response(self, data):
        count = self.page.paginator.count
        item_starting_index = self.page.start_index() - 1
        item_ending_index = self.page.end_index() - 1

        content_range = "items {0}-{1}/{2}".format(
            item_starting_index, item_ending_index, count
        )
        return Response(
            data,
            headers={
                "Content-Range": content_range,
                "X-Total-Count": count,
                "Access-Control-Expose-Headers": "X-Total-Count",
            },
        )
