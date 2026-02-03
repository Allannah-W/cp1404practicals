from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.609


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
        try:
            miles = float(self.root.ids.input_number.text)
        except ValueError:
            miles = 0
        km = miles * MILES_TO_KM
        self.output = f"{km:.5f} km"

    def handle_increment(self, change):
        """Increase/decrease miles input by 1"""
        try:
            miles = float(self.root.ids.input_number.text)
        except ValueError:
            miles = 0
        miles += change
        self.root.ids.input_number.text = str(miles)
        self.handle_calculate(self.root.ids.input_number.text)


ConvertMilesKM().run()
