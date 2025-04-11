import re
from django import template

register = template.Library()

@register.filter
def filter_tags(value):
    return re.sub(r'<[^>]+>', '', value)