from django import template

register = template.Library()

@register.filter
def invert_sort(value):
    return 'desc' if value == 'asc' else 'asc'