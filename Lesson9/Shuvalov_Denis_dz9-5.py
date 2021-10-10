class Stationery:


    def __init__(self, title='канцелярская принадлежность'):
        self.title = title

    def draw(self):
        print(f"Just start drawing {self.title}))")


class Pen(Stationery):
    def draw(self):
        print(f"Just drawing {self.title} pen")


class Pensil(Stationery):
    def draw(self):
        print(f"Just drawing {self.title} pensil")


class Marker(Stationery):
    def draw(self):
        print(f"Just drawing {self.title} marker")


stat = Stationery()
pen = Pen("Parker")
pencil = Pensil("Cohinor")
marker = Marker("Eric Krause")

office_supplies = [stat, pen, pencil, marker]

for i in office_supplies:
    i.draw()


