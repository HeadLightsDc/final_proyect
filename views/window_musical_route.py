from config import *
import tkintermapview

musical_route_bg = ctk.CTkImage(Image.open("resources\\background\\musical_route_bg.png"), size=(1920, 1080))

class Musical_route(Secundary_window):
    def __init__(self, parent, user_id):
        super().__init__(parent)
        
        self.bg_panel.configure(self, image = musical_route_bg)
        self.user_id = user_id
        # ========== map view widget========== 
        self.map_frame = ctk.CTkFrame(self, width=1283, height=882)
        self.map_widget = tkintermapview.TkinterMapView(self.map_frame, width=1283, height=882)
        self.map_widget.set_position(-24.7891876, -65.4103297) #Controla la ubicación por defecto del mapa
        self.map_widget.set_zoom(16) #Distancia de visualización del mapa
        
        self.map_frame.place(x=533, y=194)
        self.map_widget.place(x=0, y=0)
        
        # ========== button widgets ==========
        self.back_window_button = Button_theme_1(self, 
                                                 text="Volver atras",
                                                 command=lambda: self.back_window())
        
        self.back_window_button.place(x=170, y=1010)
        
        # ========== inicializacion ==========
        self.show_mark_events()
        
    def show_mark_events(self):
        with open("data/account.json", "r") as file:
            data = json.load(file)
           
        user = data["account"].get(str(self.user_id))
        event_ids = user.get("event_history")
        
        with open("data/event.json", "r") as file:
            event_data = json.load(file)
        
        for event_id in event_ids:
            event = event_data["events"].get(event_id)
            if event:
                venue = event.get("venue")
                latitude = event.get("latitude")
                longitude = event.get("longitude")
                self.map_widget.set_marker(latitude, longitude, venue)

        
    def back_window(self):
        
        """ Se autodestruye el objeto, cuando se destruye muestra el menu"""
        
        print("Cerrando ventana de añadir evento, volviendo a menu")
        self.destroy()
        