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


class CSEfreshers(CSEstudent):
    def mustEnrollment(self):
        print(self.name, "must include CSE-1211 course")


s1 = student("safaith", 20)
s1.details()
s2 = CSEstudent("fahim", 18, 7)
s2.details()
s2.cry()
s3 = CSEfreshers("tanjim", 89, 3)
s3.mustEnrollment()
s3.cry()
