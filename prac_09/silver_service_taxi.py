from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi that includes a fanciness
    attribute."""

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise silver service taxi instance."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = self.fanciness * Taxi.price_per_km

    def __str__(self):
        """Return a string like a Taxi but with current flagfall."""
        string_representation = super().__str__()
        return f"{string_representation} plus flagfall of ${self.flagfall:.2f}"

    def get_fare(self):
        """Return the price for the taxi trip."""
        fare = super().get_fare()
        return fare + self.flagfall
