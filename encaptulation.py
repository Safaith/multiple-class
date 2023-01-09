class student:
    def __init__(self, name, id):
        self.name = name
        self.__id = id

    def display(self):
        print("name: ", self.name, " id: ", self.__id)

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

# ----------------------------------------------------------------------------------------------------------------


s1 = student("safaith", 20)
s2 = student("tanjim", 18)
# s1.__id = 78
# print(s1.__dict__)
s1.set_id(78)
print(s1.get_id())

# s1.display()
# s2.display()
