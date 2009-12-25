from shopjet.my_db.models import Glossary
from django.template.defaultfilters import stringfilter
from django import template
import re
register=template.Library()


#@stringfilter
@register.filter(name='term_defenition')
def term_defenition(value):
    "glossary for common term related to a specific product"    
    glossaries = Glossary.objects.all()
    string=value
    for word in glossaries:        
        replacement = '<span class="glossary" title="%s" > %s </span>'%(word.defenition.strip(),word.term)
        string = re.sub(word.term, replacement, string)            
        
    return string
    
#register.filter('term_defenition',term_defenition)