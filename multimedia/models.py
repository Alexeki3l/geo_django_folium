from django.db import models
from django.contrib.auth.models import User
from map.models import Marker

# Create your models here.

class Multimedia(models.Model):
    # id          = models.AutoField(primary_key=True, unique=False, )
    name        = models.CharField(max_length=255, null=True, blank=True)
    file        = models.FileField()
    TYPE        = (('1', 'user'), 
                    ('2', 'marker'), 
                    #('3', 'product'),
                    )
    type        = models.CharField(max_length=1, choices=TYPE)
    users       = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="multi_user")
    markers     = models.ForeignKey(Marker, on_delete=models.CASCADE, null=True, blank=True, related_name="multi_marker")
    #products    = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True, related_name="multi_products")
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name        = "multimedia"
        verbose_name_plural = "multimedias"
        
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):

        if not self.created:
            #CREATED
            if self.type == "1":
                self.markers = None
                self.name = self.file.url.split("/")[-1].split(".")[-2]
                return super().save(self,*args,**kwargs)

            elif self.type == "2":
                self.users = None
                self.name = self.file.url.split("/")[-1].split(".")[-2]
                return super().save(self,*args,**kwargs)
#********************************************************************************
            #UPDATED
            if self.type == "1":
                self.markers = None
                self.name = self.file.url.split("/")[-1].split(".")[-2]
                return super(Multimedia,self).save(force_update=True)

            elif self.type == "2":
                self.users = None
                self.name = self.file.url.split("/")[-1].split(".")[-2]
                return super(Multimedia,self).save(force_update=True)

