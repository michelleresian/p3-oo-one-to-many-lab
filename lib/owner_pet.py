class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=''):
        self.name = name
        if (pet_type in Pet.PET_TYPES):
            self.pet_type = pet_type
        else:
            raise Exception("pet type must be one of PET TYPES")   
        self.owner = owner
        Pet.all.append(self)


class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner ==  self]

    def add_pet(self, pet):
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("Pet has to be an instance of Pet")
        
    def get_sorted_pets(self):
        return sorted([pet for pet in Pet.all if pet.owner == self], key = lambda pet: pet.name)

    
    