#coding=utf8
from django.template import Library 
from django.template.defaultfilters import stringfilter  

register = Library()  

@stringfilter 
def dytruncate(value, arg):     
    """     
    dyTruncates a string after a certain number of words including     
    alphanumeric and CJK characters.      
    Argument: Number of words to dytruncate after.     
    """     
    try:
        bits = []
        for x in arg.split(u':'):
            if len(x) == 0:
                bits.append(None)
            else:
                bits.append(int(x))
        if int(x) < len(value):
            return value[slice(*bits)] + '...'
        return value[slice(*bits)]

    except (ValueError, TypeError):
        return value 
    
register.filter('dytruncate', dytruncate)

