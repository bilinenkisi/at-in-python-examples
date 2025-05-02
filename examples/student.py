from math import isnan


class Student:
    def __init__(self, first_name: str, last_name):
        self.first_name = first_name
        self.first_name_cap = first_name.capitalize()
        self.last_name = last_name
        self.points = []

    def add_point(self, point_value):
        if not isinstance(point_value,int):
            raise TypeError("Not bir sayı değeri olmalıdır")
        if point_value < 0 or point_value > 100:
            raise ValueError("Not 0-100 arasında olmalıdır")
        self.points.append(point_value)

    def calculate_avg(self):
        if not self.points:
            return 0
        return sum(self.points) / len(self.points)

    def is_successful(self):
        return self.calculate_avg() >= 60