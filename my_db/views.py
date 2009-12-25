from django import http
from django import forms
from django.shortcuts import render_to_response
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.utils import simplejson

from models import *
import random

# gets a store url and store_product_id and return the product 
def show_product(request):
    print 'Start work'
    #if not request.method == 'GET' :
    #    raise http.Http404                
    try:
        product_id = request.GET['productId']           
        storeURL = request.GET['storeURL']      
#        mapping_obj=Mapping.objects.get(store__storeURL=storeURL, storeProductId=product_id)
        print 'Got %s : %s ' % (product_id, storeURL)
        mapping_obj=Mapping.objects.get(store__id=storeURL, product_id=product_id)
    except:
        raise http.Http404                
    #if the users shared the product with a friend 
    try:    
        tracking_id = request.GET.get('sjtc', None)
        if tracking_id:
            tracking_obj=Tracking.objects.get(trackId = tracking_id, store = mapping_obj.store )
            tracking_obj.visitor_count+=1
            tracking_obj.save()
    except Tracking.DoesNotExist:
        pass
        
    html = render_to_string('show_product.html', {'product': mapping_obj.product, 
                                                  'reviews': mapping_obj.product.productreview_set.all(), 
                                                  'photos': mapping_obj.product.photo_set.all(),
                                                  'tracking_id': str(random.random())[2:]})
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
    #return http.HttpResponse("")
    return render_to_response('test.html', {'value':'DLNASRSFull-duplexISFcccHDTV'} )
    
    

def table(request):
    products = Product.objects.all()
    data = {}
    for i in products:
        data.
    Pro


    
    
    
    
          
        
    
    
    
    
    
