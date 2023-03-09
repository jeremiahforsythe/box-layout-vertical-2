from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class ABCBoxLayout(BoxLayout):
    pass


class TheLabApp(App):
    def build(self):
        return ABCBoxLayout()


TheLabApp().run()