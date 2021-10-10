class Road:
    def __init__(self, le, wi):
        self._length = le
        self._width = wi

    def calc(self, weight=40, thickness=25):
        print(f"масса асфальта - {self._length * self._width * weight * thickness/ 1000} т")


        # return f"{self._length} м * {self._width} м * {weight} кг * {thickness} см =" \
        #        f" {(self._length * self._width * weight * thickness) / 1000} т"


def main():
    while True:
        try:
            road_1 = Road(int(input("Enter width(m): ")), int(input("Enter length(m): ")))
            road_1.calc()
            break
        except ValueError:
            print("Int")


# road_1 = Road(5000, 20)
# print(road_1.get_full_profit())
