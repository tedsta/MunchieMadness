import kivy
kivy.require('1.7.2')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

class Root(FloatLayout):
	sup = None

class MunchieMadness(App):
	pass

Factory.register('Root', cls=Root)
	
if __name__ == '__main__':
    MunchieMadness().run()
