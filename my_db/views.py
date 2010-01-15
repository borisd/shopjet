from django import http
from django import forms
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import simplejson

import local_settings

from models import *
import random

def get_table(mapping):
    display_size = Attribute.objects.filter(name__iexact='DisplaySize')[0]
    filter_category =display_size
    
#    filter_category = mapping.product.productattribute_set.all()[0].name

    size = mapping.product.productattribute_set.get(name=filter_category).value

    products = [mapping.product]
    store_mappings = mapping.store.mapping_set.all()
    for p in store_mappings:
        if p.product == mapping.product:
            continue
        if not p.product.productattribute_set.filter(name=filter_category, value=size):
            continue
        
        products.append(p.product)
        if len(products) > 3:
            break

    attrs = ProductAttribute.objects.filter(product=mapping.product).order_by("name__aclass")
    
    curr_aclass = 0
    result = []
    block = 0
    for i in attrs:
        if i.name.aclass != curr_aclass:
            if block:
                result.append(block)

            curr_aclass = i.name.aclass
            block = { 'class': curr_aclass, 'attrs': [] }

        block['attrs'].append(i.name)

    result.append(block)    

    return render_to_string('table.html', { 
        'result': result,
        'products':products,
        'product':mapping.product,
        'store': mapping.store,
        'data_site':local_settings.DATA_SITE })

def table(request):
    table = get_table(Mapping.objects.all()[71])
    return HttpResponse(table)


def gadget(request):
    pass

# gets a store url and store_product_id and return the product 
def build_html(request, mapping):
    table = get_table(mapping)

    similar = []
    for p in mapping.store.mapping_set.all():
        if p.product == mapping.product:
            continue
        similar.append(p.product)

    similar = similar[0:2]        

    html = render_to_string('show_product.html', {'product': mapping.product, 
                                                  'reviews': mapping.product.productreview_set.all(), 
                                                  'user_reviews': mapping.product.userreviews_set.all(), 
                                                  'photos': mapping.product.photo_set.all(),
                                                  'similar':similar,
                                                  'store':mapping.store,
                                                  'tracking_id': str(random.random())[2:],
                                                  'table':table,
                                                  'data_site':local_settings.DATA_SITE,})
    return html

def get_mapping(request):
    if not request.method == 'GET' :
        print 'Not a GET request'
        raise http.Http404                
    
    print request.GET

    try:
        product_id = request.GET['productId']           
        storeURL = request.GET['storeURL']      
        mapping_obj=Mapping.objects.get(store__storeURL=storeURL, storeProductId=product_id)
    except:
        print 'Could not get mapping [%s] : [%s]' % (request.GET.get('productId', '0'), request.GET.get('storeURL', '0'))
        raise http.Http404                
    return mapping_obj


def show_product(request):
    print 'Start work'

    mapping = get_mapping(request)

    html = build_html(request, mapping)

    json = simplejson.dumps({'html': html})

    return HttpResponse(request.GET['callback'] + '(' + json + ')', mimetype='application/json')

def show(request):
    mapping=Mapping.objects.get(store__storeURL='livesale.co.il', storeProductId='LG47')
    html = build_html(request, mapping)
    return HttpResponse(html)

def generate_tracking(request):
    if not request.method == 'GET' :
        raise http.Http404                
        
    storeURL = request.GET['storeURL']      
    tracking_id = request.GET['tracking_id']
    couponId = random.randint(0, 100000)
    newTracking = Tracking(trackId = tracking_id, couponId = couponId, store = Store.objects.get(storeURL=storeURL), visitor_count = 0)
    newTracking.save()
    return render_to_response('generate_tracking.html', {'couponId': couponId})
    
def tag_test(request):
    return render_to_response('test.html', {'value':'DLNASRSFull-duplexISFcccHDTV'} )


