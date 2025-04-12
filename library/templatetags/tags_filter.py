import re
from django import template

register = template.Library()

@register.filter
def filter_tags(value):
    """
    This filter removes HTML tags from a string.
    """
    return re.sub(r'<[^>]+>', '', value)