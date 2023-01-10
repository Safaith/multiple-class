class teacher:
    def __init__(self,name):
        self.name = name
        self.color = "white"
    def details(self):
        print(self.name,",thats my name")
class student(teacher):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
    def colors(self):    
        print(self.name,",thats my name and my color is ",self.color)

t1 =teacher("rashed")
s1 = student("safaith hasan","black")
t1.details()
s1.details()
s1.colors()            


