from django.db import models
from widgets import RemovableImageField
from datetime import datetime
from south.modelsinspector import add_introspection_rules
add_introspection_rules([], ["^pixelcode\.widgets\.RemovableImageField"])

class Navigation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = RemovableImageField(upload_to='images/navigations/', null=True, blank=True)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now())
    
    class Meta:
        ordering = ['order',]
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        if 'home' in self.slug:
            return ''
        return '%s/' % (self.slug)

    def save(self, *args, **kwargs):
        super(Navigation, self).save()
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

class SubNavigation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = RemovableImageField(upload_to='images/navigations/', null=True, blank=True)
    navigation = models.ForeignKey(Navigation)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now())
    
    class Meta:
        ordering = ['order',]
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        if 'home' in self.slug:
            return ''
        return '%s/%s/' % (self.navigation.slug, self.slug)

    def save(self, *args, **kwargs):
        super(SubNavigation, self).save()
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

class SubSubNavigation(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    order = models.IntegerField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    image = RemovableImageField(upload_to='images/navigations/', null=True, blank=True)
    subnavigation = models.ForeignKey(SubNavigation)
    publish = models.BooleanField(default=True)
    publish_date = models.DateTimeField(default=datetime.now())
    
    class Meta:
        ordering = ['order',]
        
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        if 'home' in self.slug:
            return ''
        return '%s/%s/%s/' % (self.subnavigation.navigation.slug, self.subnavigation.slug, self.slug)

    def save(self, *args, **kwargs):
        super(SubSubNavigation, self).save()
        try:
            ping_google()
        except Exception:
            # Bare 'except' because we could get a variety
            # of HTTP-related exceptions.
            pass

class ContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    comment = models.TextField()
    publish_date = models.DateTimeField(default=datetime.now())
    
    class Meta:
        ordering = ['publish_date']
        
    def __unicode__(self):
        return self.name
    