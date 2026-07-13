'''
#1
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
'''
#3
class Athlete:
    def __init__(self,name,age):
        self.name =name
        self.age = age 
    def introduce(self):
        print(f'{self.name} is {self.age} years old and is an athlete.')
class Cyclist(Athlete):
    def __init__(self,name,age,bike_brand):
        super().__init__(name, age)
        self.bike_brand = bike_brand
    def describe_gear(self):
        print(f'Cyclist {self.name} rides a {self.bike_brand}.')
cyclist = Cyclist('Mike',30,'Trek')
cyclist.introduce()
cyclist.describe_gear()

#4
class Athlete:
    def __init__(self,name,contry):
        self.name =name 
        self.contry=contry
    def greet(self):
        print(f'{self.name} represent {self.contry}.')
class Swimmer(Athlete):
    def __init__(self, name, contry,stroke_style):
        super().__init__(name, contry)
        self.stroke_style = stroke_style
class Runner(Athlete):
    def __init__(self, name, contry,best_distance):
        super().__init__(name, contry)
        self.best_distance = best_distance
class Cyclist(Athlete):
    def __init__(self, name, contry,race_type):
        super().__init__(name, contry)
        self.race_type = race_type
athlete = Swimmer('Lior','Israel','freestyle')
athlete.greet()
athlete = Runner('Avi','Kenya','marathon')
athlete.greet()
athlete = Cyclist('Jan','France','road')
athlete.greet()

#5
class Athlete:
    def __init__(self,name,age):
        self.name =name
        self.age = age
    def warm_up(self):
        print(f'{self.name} is warming up.')
class Gymnast(Athlete):
    def __init__(self, name, age,apparatus):
        super().__init__(name, age)
        self.apparatus= apparatus
    def compete(self):
        print(f'{self.name} is competes on {self.apparatus}.')
class Swimmer(Athlete):
    def __init__(self, name, age,stroke):
        super().__init__(name, age)
        self.stroke = stroke
    def compete(self):
        print(f'{self.name} competes in {self.stroke}')
athlete1 =Gymnast('Ana',19,'rings')
athlete1.warm_up()
athlete1.compete()
athlete2 = Swimmer('Ben',21,'butterfly')
athlete2.warm_up()
athlete2.compete()

#6
class Athlete:
    def __init__(self,name,age,years_active):
        self.name = name
        self.age = age
        self.years_active = years_active
    def experience(self):
        print(f'{self.name} has been active for {self.years_active} years.')
class TeamSportPlayer(Athlete):
    def __init__(self, name, age, years_active,team_name):
        super().__init__(name, age, years_active)
        self.team_name =team_name
    def team_info(self):
        print(f'{self.name} plays for {self.team_name}.')
player = TeamSportPlayer('Gal',28,10,'Maccabi')
player.experience()
player.team_info()

#7 
class Athlete:
    def __init__(self,name,sport):
        self.name =name
        self.sport=sport
        self.personal_best = None
    def set_record(self,value):
        self.personal_best = value
        print(f'new record {value}')
    def has_record(self):    
        return self.personal_best is not None
class Sprinter(Athlete):
    def __init__(self, name):
        super().__init__(name, sport='100m_Sprint')
s = Sprinter("Usain")
print(f"has_record() -> {s.has_record()}")
s.set_record(10.8)
print(f"has_record() -> {s.has_record()}")
print(s.personal_best)


#8
class Athlete:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.sessions_completed=0
    def train(self):
        self.sessions_completed+=1
    def session_needed(self,target):
        return max(target - self.sessions_completed, 0)
class Triathlete(Athlete):
    def __init__(self, name, age,discipline):
        super().__init__(name, age)
        self.discipline = discipline
    def describe(self):
        print(f'triathlete {self.name}, age {self.age},disciplain: {self.discipline}')

member = Triathlete('Dan',26,'cycling')
member.describe()
for _ in range(5):
    member.train()

remaining = member.session_needed(10)
print(f"{member.sessions_completed} sessions completed. {remaining} more needed.")