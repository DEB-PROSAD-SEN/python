class Person:
    name = "Amonymous"
    @classmethod
    def change_name(cls,name):
        cls.name=name

p1=Person()
p1.change_name("rahul")
print(p1.name)
print(Person.name)
