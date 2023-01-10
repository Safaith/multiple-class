class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def details(self):
        print(self.name, "thats my name, and my id is: ", self.id)


class CSEstudent(student):
    def __init__(self, name, id, labs):
        super().__init__(name, id)
        self.no_of_labs = labs

    def cry(self):
        print("cse students are cry for ", self.no_of_labs, " labs")


class BBAstudent(student):
    def chill(self):
        print("We are chilling")


s1 = student("Safaith", 20)
s2 = CSEstudent("Joynal", 18, 5)
s1.details()
s2.details()
s2.cry()
s3 = BBAstudent("Tanjim", 89)
s3.details()
s3.chill()
