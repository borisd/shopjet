from shopjet.my_db.models import Glossary
from django.template.defaultfilters import stringfilter
from django import template
from django.utils.translation import ugettext as _
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

def product_attribute(product, attrtype):
    try:
        attr = product.productattribute_set.get(name=attrtype)
    except:
        return '&nbsp'

    return _(attr.value) + ' ' + (attrtype.units)

register.simple_tag(product_attribute)

