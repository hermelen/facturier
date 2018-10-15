from django import template
register = template.Library()

@register.filter
def div(value, div):
    return round((value / div), 2)

@register.filter
def multiply(value, multiple):
    return value * multiple
