from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout

Builder.load_file('sub.kv')

class BuilderTest(BoxLayout):
	pass

class BuilderTestApp(App):
	title = "Builder Test"

	def build(self):
		app = BuilderTest()
		return app

if __name__ == "__main__":
	BuilderTestApp().run()
