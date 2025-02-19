# #savarjisho 1
# ar damisrulebia bolomde


# class People:
# def __init__(self, name, age):
# self.name = name
# self.age = age
#
# def introduce(self):
# return f"gamaejoba chemi saxelia {self.name} da me var {self.age} wlis"
#
#
# class Student(People):
# def __init__(self, name, age, id, sfero):
# super().__init__(name, age)
# self.id = id
# self.sfero = sfero
#
# def swavla(self):
# return f"{self.name} aris {self.sfero}.\n"
#
#
# class Lecturer(People):
# def __init__(self, name, age, maswavleblis_id, sagani):
# super().__init__(name, age)
# self.maswavleblis_id, = maswavleblis_id,
# self.sagani = sagani
#
# def teach(self):
# return f"{self.name} aswavlis {self.sagani}."
#
#
#
# student1 = Student("nika", 20, "123123", "programisti")
# student2 = Student("zviangi", 22, "3123123", "matematikosi")
# lecturer1 = Lecturer("nato", 45, "123321133", "musikas")
#
#
# print(student1.introduce())
# print(student1.swavla())
#
# print(student2.introduce())
# print(student2.swavla())
#
# print(lecturer1.introduce())
# print(lecturer1.teach())
#


#savarjisho 2
class LibraryItem:
def __init__(self, title, status="xelmisawvdomi"):
self.title = title
self.status = status

def booking(self):
if self.status == "xelmisawvdomi":
self.status = "dakavebuli"
return f"{self.title} warmatebit aris dajavshnili"
else:
return f"{self.title} ukve dajavshnilia"


class Book(LibraryItem):
def __init__(self, title, author, status="xelmisawvdomi"):
super().__init__(title, status)
self.author = author

def booking(self):
return super().booking()


class CD(LibraryItem):
def __init__(self, title, artist, status="xelmisawvdomi"):
super().__init__(title, status)
self.artist = artist

def booking(self):
return "CD dajavshvna ar aris xelmisawvdomi"



book1 = Book("Harry Potter", "zezva")
book2 = Book("The txa", "jemala")
cd1 = CD("Best", "idk")

print(book1.booking())
print(book1.booking())
print(cd1.booking())