from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import User
from .models import Multimedia

# Register your models here.

class MultimediaAdmin(admin.ModelAdmin):
    
    # form = ContenidoModelForm
    ordering    =   ('-updated',)
    list_display = ('img','name','username','markers','type',)
    search_fields = ['name',]
    list_filter = ['created','type',]
    # filter_horizontal = ('habilidades',)
    readonly_fields  = ("created", "updated",)

    def img(self,obj):
        
        lista = obj.file.url.split("/")
        name = lista[-1]
        ext = name.split(".")
        ext = ext[-1]
        if ext in ('jpg','jpeg','png'):
            return format_html('<img src={} width="130" height="100" />',obj.file.url )
        
        if ext in ('mp4','avi'):
            return format_html('<video src={} width="130" height="100" poster={} autoplay="True" muted="True"> </video>',obj.file.url, obj.file.url )

    def username(self, obj):
        if obj.type == '1':
            return obj.users

    def marker(self, obj):
        if obj.type == '2':
            return obj.markers
    
    

admin.site.register(Multimedia,MultimediaAdmin)
