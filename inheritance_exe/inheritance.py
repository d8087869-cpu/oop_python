class Athlete:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def introduce(self):
        print(f'{self.name} is {self.age} years old and is an athlete')
class Swimmer(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age)
s = Swimmer('Tom',25)
s.introduce()

#2
class Athlete:
    def __init__(self,name,age,sport):
        self.name = name
        self.age = age
        self.sport= sport
    def describe(self):
        print(f'{self.name} competes in {self.sport}.')
class Runner(Athlete):
    def __init__(self, name, age):
        super().__init__(name, age, sport='running')
r = Runner('sara' , 25)
r.describe()

#3