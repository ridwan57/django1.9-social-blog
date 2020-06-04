from urllib.parse import quote_plus
from django import template

register = template.Library()

@register.filter
def urlify(value):
	#return "fWRG"
    return quote_plus(value)