from django.db import models

class OutsideReview(models.Model):
    site = models.URLField()
    site_name = models.CharField(max_length=100)

    review_url = models.URLField()
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    img = models.URLField(blank=True)
    author = models.CharField(max_length=100, blank=True)
    author_url = models.URLField(blank=True)
    date = models.DateTimeField()

    model = models.CharField(max_length=100, blank=True)
    firm = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return u'%s - %s' % (self.site_name, self.title)

    class Meta:
        unique_together = (("site", "title"),)

