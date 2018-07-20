from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.lang.builder import Builder
from kivy.properties import ListProperty, StringProperty, ObjectProperty
from kivy.graphics import Color, Rectangle
from kivy.core.window import Window
from kivy.graphics import Color
from kivy.base import runTouchApp

Builder.load_file("menu.kv")

class Menu(BoxLayout):

    background_color = ListProperty()
    background_image = StringProperty()
    header_background_color = ListProperty()
    header_background_image = StringProperty()
    header_image = ObjectProperty()
    header_icon = StringProperty()
    main_box = ObjectProperty()
    header_text = ObjectProperty()
    
    def __init__(self,**kwargs):

        super(Menu,self).__init__(**kwargs)
        self.element_dict = {}
        self.is_menu_open = True
        Window.bind(on_resize = self._on_resize)
        self.hint_x = self.size_hint_x
        self.hint_y = self.size_hint_y
        self.first_header_image_height = self.header_image.height
        self.window_width = Window.width
        self.header_icon = "images/header_icon.png"
            
    def _on_resize(self,a,width,height):
        
        if self.is_menu_open == False:
            
            self.pos_hint = {"right":20/Window.width}
            
        else:

            if width <= self.window_width:
                
                if self.width <= self.header_image.height:

                    self.size_hint_x = None
                    self.width = self.header_image.height
            else:

                if self.hint_x == "None":
                    
                    self.size_hint_x = None
                    
                else:
                    self.size_hint_x = self.hint_x

            self.window_width = width
            
    def switch_menu(self):
        
        if self.is_menu_open:
            
            self.pos_hint = {"right":20/Window.width}
            self.is_menu_open = not self.is_menu_open
            self.size_hint_x = None
            
        else:
             
            self.pos_hint = {"x":0}
            if self.hint_x == "None":
                self.size_hint_x = None
            else:
                self.size_hint_x = self.hint_x
            self.is_menu_open = not self.is_menu_open
            
    def switch_sizable(self,hint_x,hint_y,width = 250,height = 1):

        self.hint_x = hint_x
        self.hint_y = hint_y

        if width < self.header_image.height:
            width = self.header_image.height
            
        if (hint_x != "None") and (hint_y != "None"):
            
            self.size_hint = (hint_x,hint_y)
            
        elif hint_x == "None" and hint_y != "None":

            self.size_hint = (None,hint_y)
            self.width = width

        elif hint_x != "None" and hint_y == "None":

            if height == 1:

                self.size_hint = (hint_x,height)

            else:

                self.size_hint = (hint_x,None)
                self.height = height

        elif (hint_x == "None") and (hint_y == "None"):

            if height == 1:

                self.size_hint = (None,height)
                self.width = width
            else:
                self.size_hint = (None,None)
                self.width = width
                self.height = height

            
    def set_background_color(self,r,g,b,a):

        self.background_color = [r,g,b,a]

    def set_background_image(self,source):

        self.background_image = source

    def set_header_background_color(self,r,g,b,a):

        self.header_background_color = [r,g,b,a]

    def set_header_background_image(self,source):

        self.header_background_image = source

    def set_header_image(self,source):

        self.header_icon = source

    def set_header_text(self,text):
        
        self.header_text.text = text
        
    def add_element(self,element_name,element_text):

        self.element = Button(text = element_text,
                              size_hint_y = None,
                              height = 30)
        self.main_box.add_widget(self.element)
        self.element_dict[element_name] = self.element

    def get_element_list(self):

        return self.element_dict

        
            
menu = Menu()

menu.switch_sizable(0.5,1,300)
menu.set_background_color(0,1,1,1)
menu.set_header_background_color(0.1,0.5,0.9,1)
menu.add_element("element_1","element_1")
menu.add_element("element_1","element_2")
menu.add_element("element_1","element_3")
menu.add_element("element_1","element_4")
runTouchApp(menu)
