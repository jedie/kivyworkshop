#!/usr/bin/env python2
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
#from paho.mqtt.client import Client
from kivy.logger import Logger
from kivy.properties import StringProperty
from kivy.clock import Clock

Builder.load_string('''
<MyWidget>:
    size: root.size
    pos: root.pos
    orientation: 'vertical'
    Label:
        text: "MQTT Connect!"
    TextInput:
        placeholder: "FOO"
        text: "127.0.0.1:1883"
    BoxLayout:
        padding: 20
        Button:
            text: "Connect"
            on_press: app.connect()
            id: connect
            disabled: not app.state != "connected"
        Button:
            text: "Disconnect"
            on_press: app.disconnect()
            disabled: not app.state != "disconnected"
            id: disconnect
''')


class MyWidget(BoxLayout):
    pass


class MyApp(App):

    state = StringProperty("disconnected")

    def build(self):
        return MyWidget(text="MQTT DEMO")

    def connect(self):
        Logger.info("Connect")
        Logger.info(str(dir(self.root.ids)))

        Clock.schedule_once(lambda *args: setattr(App.get_running_app(), "state", "connected"), 1)

    def disconnect(self):
        print("Disconnect")

MyApp().run()
