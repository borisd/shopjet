from shopjet.my_db.models import *
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

    str = _(attr.value)
    if attrtype.units:
        str += attrtype.units
    return str

def product_store_url(product, store):
    try:
        mapping = Mapping.objects.get(store__id=store.id, product__id=product.id)
    except Exception, e:
        return '#'
    return mapping.url

register.simple_tag(product_attribute)
register.simple_tag(product_store_url)

