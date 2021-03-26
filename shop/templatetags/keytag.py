from django.template import Library

register = Library()


@register.filter
def lookup(d, key):
	# To look for variable index in a list
	# print("runs.properly")
	return d[key]