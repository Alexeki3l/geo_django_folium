from django.shortcuts import render
import folium

from .utils import create_map

# Create your views here.

def viewMap(request):
    map = create_map()
    #Pincha pero no encaja bien el sitio con respecto a la pantalla
    #map_html = map._repr_html_()
    #Este si hace lo que se quiere
    map_html = map.get_root().render()
    return render(request, "map.html", {"map":map_html})
