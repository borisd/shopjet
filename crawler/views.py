# App specific import
from models import *

# Django specific imports
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required #, user_passes_text
from django.contrib.auth.models import User
from django.contrib import auth
from django.db import IntegrityError

# Utils
from datetime import datetime
import random, re
from BeautifulSoup import BeautifulSoup
import urllib2

def dtown_parse_page(data):
    soup = BeautifulSoup(data)

    reviews =  soup.findAll('div', 'short_holder')
    
    base = 'http://www.dtown.co.il/'
    skipped = 0
    done = 0

    for review in reviews:
        review_url = base + review.div.a['href']
        try:
            img = review.div.a.img['src']
        except:
            continue

        title = review.h2.a.text

        summary = review.span.text
        author = review.contents[9].contents[1].text
        author_url = base + review.contents[9].contents[1]['href']
        date = datetime.strptime(review.contents[9].contents[0][:-2].strip(), '%d/%m/%y %H:%M:%S')

        item = OutsideReview(site=base, site_name='DTown', review_url=review_url, summary=summary, 
                title=title, img=img, author=author, author_url=author_url, date=date)
        try:
            item.save()
        except IntegrityError:
            skipped += 1
        else:
            done += 1

    return done, skipped

def crawl_dtown():
    done = 0
    skipped = 0
    
    for i in range(14, 16):
        try:
            page = urllib2.urlopen("http://www.dtown.co.il/tag/lcd/index.%d.html" % i)
        except:
            continue

        print 'Fetched page %d' % i

        done_now, skipped_now = dtown_parse_page(page)
        done += done_now
        skipped += skipped_now

    return done, skipped

def index(request):

    done, skipped = crawl_dtown()

    items = OutsideReview.objects.all()

    return render_to_response('list_all.html', locals())
