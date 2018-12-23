from django import template

register = template.Library()


@register.simple_tag
def call_func(func_name, *args):
    return func_name(*args)
