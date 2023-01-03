from django.http import QueryDict
from django import template

register = template.Library()


@register.filter
def get_attr(obj, attr):
    return getattr(obj, attr)


@register.simple_tag
def merge_query_string(request, query_string, replace=True):
    request_query_dict = request.GET.copy()
    new_query_dict = QueryDict(query_string)

    # QueryDict.update의 동작은 해당 item을 대체(replace)하지 않고 덧붙이는(append) 방식임.
    # 프로젝트 내에서는 대부분의 경우 대체하는 방식으로 사용됨. (replace=True)
    # https://docs.djangoproject.com/en/3.1/ref/request-response/#django.http.QueryDict.update
    if replace:
        for key in new_query_dict.keys():
            request_query_dict.pop(key, None)

    request_query_dict.update(new_query_dict)

    return request_query_dict.urlencode()
