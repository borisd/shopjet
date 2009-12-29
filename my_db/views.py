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

    products = []
    store_mappings = mapping.store.mapping_set.all()
    for p in store_mappings:
        products.append(p)


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

    return render_to_string('table.html', { 'result': result, 'products':products, 'data_site':local_settings.DATA_SITE })

def table(request):
    table = get_table(Mapping.objects.all()[1])
    return HttpResponse(table)


# gets a store url and store_product_id and return the product 
def show_product(request):
    print 'Start work'

    if not request.method == 'GET' :
        print 'Not a GET request'
        raise http.Http404                

    try:
        product_id = request.GET['productId']           
        storeURL = request.GET['storeURL']      
        mapping_obj=Mapping.objects.get(store__storeURL=storeURL, storeProductId=product_id)
    except:
        print 'Could not get mapping [%s] : [%s]' % (request.GET.get('productId', '0'), request.GET.get('storeURL', '0'))
        raise http.Http404                

    #if the users shared the product with a friend 
    try:    
        tracking_id = request.GET.get('sjtc', None)
        if tracking_id:
            tracking_obj=Tracking.objects.get(trackId = tracking_id, store = mapping_obj.store )
            tracking_obj.visitor_count+=1
            tracking_obj.save()
    except Tracking.DoesNotExist:
        print 'Could not get traking'
        pass
        

    print 'Start render'
    table = get_table(mapping_obj)
    html = render_to_string('show_product.html', {'product': mapping_obj.product, 
                                                  'reviews': mapping_obj.product.productreview_set.all(), 
                                                  'photos': mapping_obj.product.photo_set.all(),
                                                  'tracking_id': str(random.random())[2:],
                                                  'table':table,
                                                  'data_site':local_settings.DATA_SITE,})
    json = simplejson.dumps({'html': html})
    return HttpResponse(request.GET['callback'] + '(' + json + ')', mimetype='application/json')
    
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


