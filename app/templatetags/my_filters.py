from django import template

register = template.Library()


@register.filter
def list_split(import_list: list):
    return import_list[0].split(';')


@register.filter
def float_make(element):
    return float(element)
