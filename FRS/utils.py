from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination


class SetPagination(PageNumberPagination):
    page_size_query_param = 'offset'
    max_page_size = 10
    page_size = 5
