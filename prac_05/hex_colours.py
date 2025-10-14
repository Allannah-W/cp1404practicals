colour_name_to_hex = {"Absolute Zero": "#0048ba",
                      "Acid Green": "#b0bf1a",
                      "Alizarin Crimson": "#e32636",
                      "Amaranth": "#e52b50",
                      "Amber": "#ffbf00",
                      "Amethyst": "#9966cc",
                      "Apricot": "#fbceb1",
                      "Aqua": "#00ffff",
                      "Army Green": "#4b5320",
                      "Arylide Yellow": "#e9d66b"}

colour_name = input("Colour Name: ").title()
while colour_name != " ":
    try:
        print(f"{colour_name} - {colour_name_to_hex[colour_name]}")
    except KeyError:
        print("Invalid Colour Name")
    colour_name = input("Colour Name: ").title()
