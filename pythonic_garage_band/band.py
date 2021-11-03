from abc import ABC , abstractmethod
class Band():
    instances = []
    def __init__(self,name ,members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def play_solos(self):
        solo = []
        for i in self.members:
           solo.append(i.play_solo)        
        return solo

    @classmethod
    def to_list(cls):
        return cls.instances
    @abstractmethod
    def __str__(self):
        return self.name
    @abstractmethod
    def __repr__(self):
        return self.name
    


class Musician():
    musician_list =[]

    def __init__(self, name):
         self.name= name         
     
    @classmethod
    def get_members(self):
         return self.musician_list  
     
    @abstractmethod
    def get_instrument(self):
         pass
    @abstractmethod   
    def play_solo(self) :
         pass  
    @abstractmethod      
    def __str__(self) :
         pass    
    @abstractmethod      
    def __repr__(self): 
         pass   

class Guitarist(Musician):
    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"

    def get_instrument(self):
        return "guitar"

    def play_solo(self):
        return "face melting guitar solo"

class Bassist(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"

    def get_instrument(self):
        return "bass"

    def play_solo(self):
        return "bom bom buh bom"

class Drummer(Musician):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"

    def get_instrument(self):
        return "drums"

    def play_solo(self):
        return "rattle boom crash"
