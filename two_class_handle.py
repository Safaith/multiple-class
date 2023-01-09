class student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
# --------------------------------------------------------------------------------------------------------


class common:
    def __init__(self):
        self.location = 0

    def moderate(self, std):
        self.location = std


# --------------------------------------------------------------------------------------------------------
s1 = student("safaith", 20)
c1 = common()

c1.moderate(s1)
print(c1.location)  # memory location of s1 in c1
print(c1.location.name)  # name and id print in c1 , of s1
print(c1.location.id)  # coz, c1 have s1's memory location
