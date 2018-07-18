from kivy.uix.label import Label
from kivy.lang.builder import Builder
from kivy.clock import Clock

Builder.load_file("toastmessage.kv")

class ToastMessage(Label):

    def __init__(self,message,time):

        super(ToastMessage,self).__init__()
        self.text = message
        Clock.schedule_once(self.self_deletion,time)

    def self_deletion(self,arg):

        self.parent.remove_widget(self)


