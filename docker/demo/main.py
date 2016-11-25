from kivy.uix.label import Label
from kivy.app import App

class MyApp(App):
    def build(self):
        return Label(text="Dockerized build test")

if __name__ == '__main__':
    MyApp().run()
