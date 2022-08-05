import numpy as np

class Veterinarian:
    pets = []
    def accept(self, petName):
        self.pets.append(petName)

    def heal(self):
        try:
            return self.pets.pop(0)
        except IndexError:
            pass

if __name__ == "__main__":
    veterinarian = Veterinarian()
    veterinarian.accept("Barkley")
    veterinarian.accept("Mittens")
    print(veterinarian.heal())
    print(veterinarian.heal())