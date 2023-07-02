from django.db import models
from django.urls import reverse

# Create your models here.
class TypeMarker(models.Model):
    name    = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name    = "type_marker"
        verbose_name_plural = "type_markers"
        ordering = ['-created']
        
    def __str__(self):
        return self.name



class Marker(models.Model):
    location = models.CharField(max_length=255)
    decription = models.TextField(max_length=500)
    latitude = models.FloatField()
    longitude = models.FloatField()
    #media   = models.models.ForeignKey(Multimedia, verbose_name=_("media_marker"), on_delete=models.CASCADE)
    #image   = models.ImageField(upload_to='marker',max_length=500)
    typ_e   = models.ManyToManyField(TypeMarker, related_name='type_marker')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name    = "marker"
        verbose_name_plural = "markers"
        ordering = ['-created']
    def __str__(self):
        return self.location
    #def get_absolute_url(self):
    #    return reverse('productos_details', kwargs={'pk': self.pk})

    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        
    def get_absolute_url(self):
        return reverse('home')
