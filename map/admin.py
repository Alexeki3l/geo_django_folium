from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import Marker, TypeMarker
from multimedia.models import Multimedia

# Register your models here.
class ContenidoModelForm( forms.ModelForm ):
    # Que el charfield "contenido" se comporte como un textarea
    descripcion = forms.CharField( widget=forms.Textarea )

class TypeMarkerAdmin(admin.ModelAdmin):
    ordering     = ('created',)
    list_display = ('name',)
    readonly_fields  = ('created', 'updated',)


class MarkerAdmin(admin.ModelAdmin):
    #form = ContenidoModelForm
    ordering     = ('created',)
    list_display = ('img_marker','location','latitude', 'longitude', )
    readonly_fields  = ('created', 'updated',)
    
    def img_marker(self,obj):
        #lista = list(obj.multimedia_set.all())
        multimedias = Multimedia.objects.filter(markers = obj)
        if multimedias:
            return format_html('<img src={} width="130" height="100" />',list(multimedias)[0].file.url)
        else:
            return format_html('<img src='' width="130" height="100" />')
        
admin.site.register(Marker,MarkerAdmin)
admin.site.register(TypeMarker,TypeMarkerAdmin)