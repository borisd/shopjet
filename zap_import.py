# Get DJANGO environment up
import settings
from django.core.management import setup_environ
setup_environ(settings)

from my_db.models import *
import csv, time

def import_attributes(file):
    map = {}
    defac = AttributeClass.objects.all()[0]
    reader = csv.reader(open(file, 'rb'))

    for row in reader:
        id,name,desc,units = row
        if units == 'NULL':
            units = None
        try:
            attr = Attribute.objects.get(name__iexact=name)
        except Attribute.DoesNotExist:
            # Create new entry
            attr = Attribute(name=name, desc=desc, units=units, aclass=defac)
            attr.save()
            print 'Added attribute %s' % name
        else:
            print 'Duplicate attribute %s' % name
        map[int(id)] = attr.id

    return map    

def import_stores(file):
    reader = csv.reader(open(file, 'rb'))
    map = {}
    for row in reader:
        id, name, domain = row[:3]
        try:
            store = Store.objects.get(storeName__iexact=name)
        except Store.DoesNotExist:
            store = Store(storeName=name, storeURL=domain)
            store.save()
            print 'Added new store %s' % name
        else:
            print 'Duplicate store %s' % name

        map[int(id)]=store.id    

    return map

def import_products(file):
    reader = csv.reader(open(file, 'rb'))
    map = {}
    for row in reader:
        zapid, category, manufacturer, family, model, image = row
        try:
            prod = Product.objects.get(title__iexact=manufacturer, subtitle__iexact=model)
        except Product.DoesNotExist:
            prod = Product(title=manufacturer, subtitle=model, description='', zapid=int(zapid), rating=0)
            prod.save()

            # Add tag
            try: 
                tag = Tag.objects.get(name__iexact=category)
            except Tag.DoesNotExist:
                tag = Tag(name=category)
                tag.save()
                print 'Added new tag %s' % tag

            ptag = ProductTag(product=prod, tag=tag)
            print 'Added new product %s' % prod
        else:
            print 'Duplicate product %s' % prod

        # for now we skip zap images
        continue


        if image == 'http://img.zap.co.il/pics/.gif':
            continue

        try:
            photo = Photo.objects.get(product=prod)
        except Photo.DoesNotExist:

            image = 'http://static.shopjet.co.il/static/images/%s.gif'
            
            photo = Photo(photo_small=image, product=prod, photoId=1)
            photo.save()
            print 'Added photo'
        else:
            if not photo.photo_small:
                photo.photo_small = image
                photo.save()
                print 'Added Small photo'

def import_prod_attribute(file, attr_map):
    reader = csv.reader(open(file, 'rb'))
    map = {}
    skipped = 0
    for row in reader:
        zapid, attr_id, value = row[1:4]
        if value == 'NULL':
            skipped =+ 1
            print 'Skipping attr due to NULL'
            continue

        attr = Attribute.objects.get(id=attr_map[int(attr_id)])
        try:
            prod = Product.objects.get(zapid=int(zapid))
        except Product.DoesNotExist:
            print 'ERROR: Could not find product with ID %s' % zapid
            continue


        try:
            pa = ProductAttribute.objects.get(product=prod, name=attr)
        except ProductAttribute.DoesNotExist:
            pa = ProductAttribute(product=prod, name=attr, value=value)
            pa.save()
            print '%d: Added new Product Attribute %s to %s = %s' % (pa.id, attr, prod, value)
        else:
            print '%d: Duplicate Product Attribute %s for %s' % (pa.id, attr, prod)
    print '\n\nSkipped %s\n\n' % skipped            

def import_mapping(file, store_map):
    reader = csv.reader(open(file, 'rb'))
    map = {}
    for row in reader:
        zapid, storeid, store_prod_id, store_prod_url, image = row[1:6]
        store = Store.objects.get(id=store_map[int(storeid)])
        prod = Product.objects.get(zapid=int(zapid))

        try:
            map = Mapping.objects.get(store=store, product=prod)
        except Mapping.DoesNotExist:
            map = Mapping(store=store, storeProductId=store_prod_id, product=prod, url=store_prod_url)
            map.save()
            print 'Added new Mapping for %s' % prod
        else:
            print 'Duplicate Mapping for %s' % prod
    
        try:
            photo = Photo.objects.get(product=prod)
        except Photo.DoesNotExist:
            photo = Photo(photo_large=image, product=prod, photoId=1)
            photo.save()
            print 'Added photo'
        else:
            if not photo.photo_large:
                photo.photo_large = image
                photo.save()
                print 'Added large photo'

def import_reviews(file):
    reader = csv.reader(open(file, 'rb'))
    map = {}
    for row in reader:
        author, date_str = row[1:3]
        text = reader.next()[0]
        zapid = reader.next()[1]

        prod = Product.objects.get(zapid=int(zapid))
        date = time.strptime(date_str, "%Y-%m-%d")
        try:
            review = UserReviews.objects.get(product=prod, user=author)
        except UserReviews.DoesNotExist:
            review = UserReviews(product=prod, user=author, review=text[:999], date=date)
            review.save()
            print 'Added new review for %s by %s' % (prod, author)
        else:
            print 'Duplicate review for %s by %s' % (prod, author)


def import_attribute_desc(file, attr_map):
    reader = csv.reader(open(file, 'rb'))
    map = {}

    for row in reader:
        attr_id, lang, label = row[0:3]
        desc = ','.join(row[3:])

        attr = Attribute.objects.get(id=attr_map[int(attr_id)])

        if desc != 'NULL':
            attr.desc = desc
            print 'Update desc of %s' % attr

        attr.save()


attr_map = import_attributes('zap_db\\Attributes.csv')
# store_map = import_stores('zap_db\\Stores.csv')
# import_products('zap_db\\Products.csv')
# import_prod_attribute('zap_db\\ProductsAttributes.csv', attr_map)
# import_mapping('zap_db\\StoreProducts.csv', store_map)
# import_reviews('zap_db\\Comments.csv')
import_attribute_desc('zap_db\\AttributesDescriptions.csv', attr_map)
