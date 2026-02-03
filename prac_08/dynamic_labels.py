from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Creates labels from a list of names"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Abby", "Frank", "Sarah", "Tom"]

    def build(self):
        """Build interface and labels dynamically"""
        self.root = Builder.load_file("dynamic_labels.kv")
        container = self.root.ids.main

        for name in self.names:
            label = Label(text=name)
            container.add_widget(label)

        return self.root


DynamicLabelsApp().run()
