from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty


class ConvertMilesKM(App):
    """ ConvertMilesKM is a Kivy App for converting miles to km's """

    output = StringProperty("")

    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self, value):
        """Convert miles to km"""
        miles = float(self.root.ids.input_number.text)
        km = miles * 1.609
        self.output = f"{km:.5f} km"

    def handle_increment(self, change):
        """Increase/decrease miles input by 1"""
        miles = float(self.root.ids.input_number.text)
        miles += change
        self.root.ids.input_number.text = str(miles)


ConvertMilesKM().run()
