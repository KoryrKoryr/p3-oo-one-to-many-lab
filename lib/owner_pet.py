class Pet:
    # Class attributes
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate the pet type
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Add the pet to the global list of all pets
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name} type={self.pet_type}>"

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Add a pet to the owner. Validate the pet type."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by their name."""
        return sorted(self.pets(), key=lambda pet: pet.name)

    def __repr__(self):
        return f"<Owner name={self.name}>"
