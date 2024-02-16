from django import template

register = template.Library()

@register.filter(name='split')
def split(value,key= ' '):
    return value.split(key)

@register.filter(name='times')
def times(count):
    return range(count)

@register.filter(name='filter_range')
def filter_range(start,finish):
    return range(start,finish)