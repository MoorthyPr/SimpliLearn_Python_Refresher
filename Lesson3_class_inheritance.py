class Animals:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"{self.name} the {self.species} makes a sound"


class Dog(Animals):
    def __init__(self,name,breed):
        super().__init__(name,"Dog")
        self.breed = breed

    def fetch(self):
        return f"{self.name} the {self.breed} fetches the ball!"
    


dog1 = Dog("Buddy","Golden Retriever")
print(dog1.make_sound())
print(dog1.fetch())


dog2 = Dog("Max","German Shepherd")
print(dog2.make_sound())
print(dog2.fetch())