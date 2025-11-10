from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class ConvertMilesKM(App):
    """ ConvertMilesKM is a Kivy App for converting miles to km's """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root


ConvertMilesKM().run()
