from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import Marker
from .utils import create_map
import folium
from .utils import *

# Create your views here.

def viewMap(request):
    map = create_map()
    markers = Marker.objects.all()
    if request.method == 'POST':
        if str(request.POST.get('ubicacion')):
            cadena = str(request.POST.get('ubicacion')).replace(" ","")
            cadena = str(cadena).split(':')
            latitude = float(cadena[1][:7])
            longitude = float(cadena[2])
            icon = folium.Icon(color="red")
            user_location = folium.Marker(
                        [latitude, longitude],
                        icon=icon,
                        popup = f""" <h4 class='text-mute'> Mi ubicacion</h4>""").add_to(map)
            distancias = []
            for marker in markers:
                dist = distancia(latitude, longitude,
                            marker.latitude, marker.longitude)
                distancias.append(dist)
            
            # distancias.sort()
            n =0
            while n < 3:
                indice_min = distancias.index(min(distancias))
                minimo = min(distancias)
                minimo = round(minimo, 2)
                ubicacion_mas_cercana = list(markers)[indice_min]
                
                marke = folium.Marker(
                            [ubicacion_mas_cercana.latitude, ubicacion_mas_cercana.longitude], 
                            popup = f""" <h4 class='text-mute'> {ubicacion_mas_cercana.location} </h4> <p> Distancia:{minimo} Kilometros</p><p> {ubicacion_mas_cercana.decription}</p>
                                {get_multimedia_marker(marker=ubicacion_mas_cercana, distacia=minimo)}""",
                            tooltip= 'Haz click en mi!',
                            draggable=False,
                            icon = folium.Icon(color="purple")
                            ).add_to(map)
                distancias.pop(indice_min)
                n+=1
            map.zoom = 19
        else:
            if markers:
                for marker in markers:
                    # group = folium.FeatureGroup(name=(list(marker.typ_e.all())[0]).name, show=False).add_to(map)
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
    elif request.method == 'GET':
        if markers:
            for marker in markers:
                
                # group = folium.FeatureGroup(name=(list(marker.typ_e.all())[0]).name, show=False).add_to(map)
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
    map_html = map.get_root().render()
    return render(request, "map.html", {"map":map_html})





