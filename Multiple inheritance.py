class teacher:
    def __init__(self):
        print("this is __init__ of teacher")

    def method1(self):
        print("this is method1 of teacher")


class student:
    def __init__(self):
        print("this is __init__ of student")

    def method1(self):
        print("this is method1 of student")


class assistant(teacher, student):
    def __init__(self):
        #   print("this is __init__ of assistant")
        student.__init__(self)

    def method2(self):
        print("this id method2 of assistant")


a1 = assistant()
a1.method1()
student.method1(a1)
