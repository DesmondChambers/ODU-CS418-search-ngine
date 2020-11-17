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


class History(models.Model):
    username =  models.TextField(blank=True, null=True)
    search_term = models.TextField(blank=True, null=True)
    viewed_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s viewed: %s" %(self.search_term, self.viewed_on)

    class Meta:
        verbose_name_plural = 'Histories'

class Searchsave(models.Model):
    username =  models.TextField(blank=True, null=True)
    title=models.TextField(blank=True, null=True)
    contributor_author=models.TextField( blank=True, null=True)
    description_abstract=models.TextField( blank=True, null=True)
    subject=models.TextField( blank=True, null=True)
    contributor_department=models.TextField(blank=True, null=True)
    relation_haspart=models.TextField(blank=True, null=True)
    contributor_committeechair=models.TextField(blank=True, null=True)
    date_available=models.DateTimeField(blank=True, null=True)
    
    def save(self,*args, **kwargs):
        super(Searchsave,self).save(*args, **kwargs)

    def __str__(self):
        return '%s' % (self.username,self.title)

    class Meta:
        verbose_name_plural = 'Searchsave'