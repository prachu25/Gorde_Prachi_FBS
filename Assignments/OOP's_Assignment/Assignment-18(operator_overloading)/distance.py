class Distance:

    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __add__(self, d):
        cm1 = self.km * 100000 + self.m * 100 + self.cm
        cm2 = d.km * 100000 + d.m * 100 + d.cm

        total = cm1 + cm2

        return Distance(total // 100000,
                        (total % 100000) // 100,
                        total % 100)

    def __sub__(self, d):
        cm1 = self.km * 100000 + self.m * 100 + self.cm
        cm2 = d.km * 100000 + d.m * 100 + d.cm

        total = cm1 - cm2

        return Distance(total // 100000,
                        (total % 100000) // 100,
                        total % 100)

    def display(self):
        print(self.km, "km", self.m, "m", self.cm, "cm")

    def __del__(self):
        print("Object deleted")