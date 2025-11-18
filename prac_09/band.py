class Band:
    """Band class."""
    def __init__(self, name=""):
        self.name = name
        self.musicians = []

    def __str__(self):
        """Returns string of band and musicians."""
        musicians = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians})"

    def add(self, musician):
        """Add musician to band."""
        self.musicians.append(musician)

    def play(self):
        """Print string of each musician and what instrument they play."""
        for musician in self.musicians:
            print(musician.play())
