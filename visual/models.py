from django.db import models

class Content(models.Model):
    end_year = models.CharField(max_length=100,null=True,blank=True)
    intensity = models.CharField(max_length=100,null=True,blank=True)
    sector = models.CharField(max_length=100,null=True,blank=True)
    topic = models.CharField(max_length=100,null=True,blank=True)
    insight = models.CharField(max_length=250,null=True,blank=True)
    url = models.TextField(max_length=550,null=True,blank=True)
    region = models.CharField(max_length=100,null=True,blank=True)
    start_year = models.CharField(max_length=100,null=True,blank=True)
    impact = models.CharField(max_length=100,null=True,blank=True)
    added = models.CharField(max_length=100,null=True,blank=True)
    published = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    relevance = models.CharField(max_length=100,null=True,blank=True)
    pestle = models.CharField(max_length=100,null=True,blank=True)
    source = models.CharField(max_length=250,null=True,blank=True)
    title = models.TextField(max_length=500,null=True,blank=True)
    likelihood = models.CharField(max_length=100,null=True,blank=True)
    def __repr__(self):
        return self.title
     