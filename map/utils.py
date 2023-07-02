# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36
from folium.plugins import MousePosition, LocateControl, FloatImage, Search
from folium.raster_layers import VideoOverlay
from geopy.geocoders import Nominatim as nom
import folium
import threading

from .models import Marker, TypeMarker
from multimedia.models import Multimedia

# def adicionar_popup(group, marker):
#     group.add_child(marke)

#def create_map(latitude=21.92972, longitude=-79.4425):
def create_map(latitude=None, longitude=None):
    coor = [latitude, longitude]
    if latitude and longitude:
        map = folium.Map(coor)
    map = folium.Map()
    markers = Marker.objects.all()
    type_markers_name = list(element.name for element in TypeMarker.objects.all())
    #Para hacer grupos dentro de las capas
    #group = folium.FeatureGroup(name='Universidades').add_to(map)
    liste = []
    group = ''
    
    
    map.fit_bounds(
        [[18.771115, -86.846923], [24.776759, -72.037353]], 
        max_zoom=10
        )
    
    #Crea Popus en el mapa con un click
    folium.ClickForMarker().add_to(map)
    
    #positon:'topleft', 'topright', 'bottomleft' or 'bottomright'
    folium.LayerControl(position='topright', collapsed=True).add_to(map)
    #folium.Marker
    return map

def get_multimedia_marker(marker, distacia =None):
    
    multimedias = list(Multimedia.objects.filter(markers=marker))
    if multimedias:
        html = ''
        for multimedia in multimedias:
            html += f"""
                    <div class="carousel-item active">
                        <img src="{multimedia.file.url}" class="d-block rounded-3" width='150' height='150'">
                    </div>"""
        return f"""<div id="carouselExample" class="carousel slide">
                            <div class="carousel-inner">
                                {html}
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExample" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExample" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>"""
        #return  f"<img src='{multimedias[0].file.url}' width='150' height='150' />"
    return " "

def get_icons_type_marker(marker):
    type_markers = marker.typ_e.all()
    for element in type_markers:
        if 'Punto de Carga' in element.name:
            return folium.Icon(color="blue", icon="plus-sign")
        # if 'Universidad' in element.name:
        #     return folium.Icon(color="blue", icon="pencil")
        # elif 'Centro Nocturno' in element.name:
        #     return folium.Icon(color="purple", icon="glass")
        # elif 'Restaurante' in element.name:
        #     return folium.Icon(color="beige", icon="cutlery")
        # elif 'Museo' in element.name:
        #     return folium.Icon(color="darkblue", icon="book")
        # elif 'Cafeteria' in element.name:
        #     return folium.Icon(color="darkblue", icon="compressed")
        # elif 'Hospital' in element.name:
        #     return folium.Icon(color="red", icon="plus-sign")

import math

# Función para calcular la distancia entre dos puntos en términos de latitud y longitud
def distancia(lat1, lon1, lat2, lon2):
    radio_tierra = 6371  # en kilómetros
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    a = math.sin(dlat / 2) * math.sin(dlat / 2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon / 2) * math.sin(dlon / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = radio_tierra * c
    return d

# Ubicación de la que deseas encontrar el punto más cercano
# lat1 = 40.7128
# lon1 = -74.0060

# # Lista de ubicaciones
# # ubicaciones = [
# #     {'nombre': 'Nueva York', 'lat': 40.7128, 'lon': -74.0060},
# #     {'nombre': 'Los Ángeles', 'lat': 34.0522, 'lon': -118.2437},
# #     {'nombre': 'Chicago', 'lat': 41.8781, 'lon': -87.6298},
# #     {'nombre': 'Houston', 'lat': 29.7604, 'lon': -95.3698},
# #     {'nombre': 'Miami', 'lat': 25.7617, 'lon': -80.1918}
# # ]

# Calcular la distancia entre la ubicación dada y cada una de las ubicaciones en la lista
# distancias = []
# for maker in Marker.objects.all():
#     dist = distancia(lat1, lon1, maker.latitude, maker.longitude)
#     distancias.append(dist)

# # Obtener la ubicación más cercana
# indice_min = distancias.index(min(distancias))
# ubicacion_mas_cercana = ubicaciones[indice_min]

# # Mostrar la ubicación más cercana
# print('La ubicación más cercana a ({}, {}) es {} (distancia: {} km)'.format(lat1, lon1, ubicacion_mas_cercana['nombre'], min(distancias)))