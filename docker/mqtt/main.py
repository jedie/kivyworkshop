from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen
from kivy.factory import Factory

class MqtttMainWidget(ScreenManager):
    def __init__(self, ):
        super(MqtttMainWidget, self).__init__()


class MqttApp(App):
    def build(self):
        return MqtttMainWidget()


if __name__ == '__main__':
    MqttApp().run()
