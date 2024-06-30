class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Invalid pet type. Pet must be an instance of the Pet class.")
        pet.owner = self
        self._pets.append(pet)
    
    def pets(self):
        return self._pets
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type. Pet type must be one of the following: " + ", ".join(self.PET_TYPES))
        self.name = name
        self.pet_type = pet_type
        self.owner = None  # Initialize owner to None
        Pet.all.append(self)
        if owner:
            owner.add_pet(self)  # Use the add_pet method to set the owner