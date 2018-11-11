from django import template

register = template.Library()


@register.filter(name='my_slice')
def my_slice(value, arg):
    return value[int(arg)]