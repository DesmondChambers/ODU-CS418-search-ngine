from django.db import models
from django.utils.text import slugify

# Create your models here.

class Search(models.Model):
    contributor_author = models.CharField(max_length=255, blank=True, null=True)
    description_abstract = models.TextField(blank=True, null=True)
    identifier_uri = models.TextField(blank=True, null=True)
    slug = models.SlugField(default='', blank=True)
    

    def save(self):
        self.slug = slugify(self.contributor_author)
        super(Search, self).save()
    
    
    def __str__(self):
        return '%s' % self.contributor_author
