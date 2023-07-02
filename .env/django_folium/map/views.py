from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Marker
from .utils import create_map
import folium
from .utils import *

# Create your views here.

def viewMap(request):
    map = create_map()
    #Pincha pero no encaja bien el sitio con respecto a la pantalla
    #map_html = map._repr_html_()
    markers = Marker.objects.all()
    if markers:
        for marker in markers:
            print(marker)
            group = folium.FeatureGroup(name=(list(marker.typ_e.all())[0]).name, show=False).add_to(map)
            tooltip = 'Haz click en mi!'
            get_icons_type_marker(marker)
            popup = f""" <h4 class='text-mute'> {marker.location} </h4> <p> {marker.decription}</p>
                        {get_multimedia_marker(marker=marker)}"""
            
            marke = folium.Marker(
                    [marker.latitude, marker.longitude], 
                    popup=popup,
                    tooltip=tooltip,
                    draggable=False,
                    icon = get_icons_type_marker(marker)
                    ).add_to(map)
    
    
    #Este si hace lo que se quiere
    map_html = map.get_root().render()
    return render(request, "map.html", {"map":map_html})


def adicionar_usuario(request):
    map = create_map()
    if request.method == 'POST':
        cadena = str(request.POST.get('ubicacion')).replace(" ","")
        cadena = str(cadena).split(':')
        latitude = float(cadena[1][:7])
        longitude = float(cadena[2])
        print(latitude, longitude)
        icon = folium.Icon(color="red")
        marke = folium.Marker(
                    [latitude, longitude],
                    icon=icon,
                    popup = f""" <h4 class='text-mute'> Mi ubicacion</h4>""").add_to(map)
        map.zoom = 19
        
    map_html = map.get_root().render()
    return render(request, "map.html", {"map":map_html})



