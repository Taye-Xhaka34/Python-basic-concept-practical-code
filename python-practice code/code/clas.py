#create a class human a) with properties name,age,grade
class Human:
    name = ""
    age = ""
    grade = ""
    #behaviors: running,dancing,eating
    def running(self):
        return "humam is running"
    def dancing(self):
        return "human is dancing"
    def eating(self):
        return "human is eating"
#creating object of human1
human1 = Human()
human1.name = "John"
human1.age = 25
human1.grade = "A"
print(human1.name)
print(human1.age)
print(human1.grade)