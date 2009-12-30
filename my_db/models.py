from django.db import models
from django.utils.translation import ugettext as _

class ProductReview(models.Model):
    product= models.ForeignKey("Product")
    title= models.CharField(max_length=200)
    details= models.TextField(max_length=10000)
    link = models.URLField()    
    def __unicode__(self):
        return _(self.title)
        
class Photo(models.Model):
    photo_small = models.URLField(blank=True, null=True)
    photo_large = models.URLField(blank=True, null=True)
    photoId = models.IntegerField()
    product = models.ForeignKey("Product")
    def __unicode__(self):
        return u'%s [%d]' % (self.product, self.photoId)


class Product(models.Model):
    title = models.CharField(max_length=100)    
    subtitle = models.CharField(max_length=100, blank=True, null=True)    
    video = models.URLField(blank=True, null=True)    
    features_list = models.TextField()    
    description = models.TextField(max_length=10000)
     
    def __unicode__(self):
        return _(self.title)
        
class Store(models.Model):
    storeName = models.CharField(max_length=50)
    storeURL = models.CharField(max_length=100)    
    def __unicode__(self):
        return _(self.storeName)
    
class Tracking(models.Model):
    trackId = models.CharField(max_length=30)
    couponId = models.CharField(max_length=30)
    store = models.ForeignKey(Store)
    visitor_count = models.IntegerField(default=0)
    def __unicode__(self):
        return _(self.trackId)
    
class Mapping(models.Model):
    store = models.ForeignKey(Store)
    storeProductId = models.CharField(max_length=30)
    product = models.ForeignKey(Product)
    url = models.URLField()

class Glossary(models.Model):
    term = models.CharField(max_length=100)
    defenition = models.TextField(max_length=1000)
    def __unicode__(self):
        return _(self.term)

class AttributeClass(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return _(self.name)

class Attribute(models.Model):
    name = models.CharField(max_length=30)
    desc = models.TextField(max_length=1000)
    units = models.CharField(max_length=10, blank=True, null=True)
    aclass = models.ForeignKey(AttributeClass)

    def __unicode__(self):
        return _(self.name)

class ProductAttribute(models.Model):
    product = models.ForeignKey(Product)
    name = models.ForeignKey(Attribute)
    value = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s - %s : %s' % (self.product, self.name, self.value)

class UserReviews(models.Model):
    product = models.ForeignKey(Product)
    user = models.CharField(max_length=50)
    review = models.TextField(max_length=1000)
    date = models.DateField(auto_now_add=True)

    def __unicode__(self):
        return u'%s - %s' % (self.product, self.user)
