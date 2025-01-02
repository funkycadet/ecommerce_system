from rest_framework.pagination import PageNumberPagination


class CustomPagePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 20
    page_query_param = "page"


class CustomLimitPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "limit"
    max_page_size = 20
    page_query_param = "offset"

