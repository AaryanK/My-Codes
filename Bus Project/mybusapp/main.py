from kivymd.app import MDApp
from kivy_garden.mapview import MapView
from kivy_garden import mapview
from test import give_location
class naybusApp(MDApp):
	def build(self):
		Map = MapView(zoom=13,lat=give_location()[0],lon=give_location()[1])
		marker = mapview.MapMarkerPopup(lat=give_location()[0],lon=give_location()[1],source ="bus_marker.png")
		Map.add_widget(marker)
		return Map

naybusApp().run()
