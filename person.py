import random
# random.seed(42)
from virus import Virus


class Person(object):
    # Define a person. 
    def __init__(self, _id, is_vaccinated, infection = None):
        # A person has an id, is_vaccinated and possibly an infection
        self._id = _id  # int
        self.is_vaccinated = is_vaccinated
        self.infection = infection
        self.infected = infection is not None
        self.is_alive = True
        

    def did_survive_infection(self):

        if self.infection:
            
            # random generator for survival rate
            survival_rate = random.random()

            # compareit to mortality rate
            if survival_rate < self.infection.mortality_rate:

                # if the person passes away, return false
                self.is_alive = False
                return False
            
            else:

                # if person is vaccinated, the person survived
                self.is_alive = True
                self.is_vaccinated = True
                self.infection = None
                return True
            
        return True
        

if __name__ == "__main__":
    # This section is incomplete finish it and use it to test your Person class

    vaccinated_person = Person(1, True)
    assert vaccinated_person._id == 1
    assert vaccinated_person.is_alive is True
    assert vaccinated_person.is_vaccinated is True
    assert vaccinated_person.infection is None

    # Create an unvaccinated person and test their attributes
    unvaccinated_person = Person(2, False)
    assert unvaccinated_person._id == 2
    assert unvaccinated_person.is_alive is True
    assert unvaccinated_person.is_vaccinated is False
    assert unvaccinated_person.infection is None

# Test an infected person. An infected person has an infection/virus
# Create a Virus object to give a Person object an infection
    virus = Virus("Dysentery", 0.7, 0.2)

    infected_person = Person(3, False, virus)
    assert infected_person._id == 3
    assert infected_person.is_alive is True
    assert infected_person.is_vaccinated is False
    assert infected_person.infection is virus

    # You need to check the survival of an infected person. Since the chance
    # of survival is random you need to check a group of people. 
    # Create a list to hold 100 people. Use the loop below to make 100 people

    people = []
    for i in range(1, 100): #ask if code should be changed to 101 for the range.
        person = Person(i, False, virus)
        people.append(person)

    did_survive = 0
    did_not_survive = 0

    for person in people:

        if person.did_survive_infection():
            assert person.is_alive
            assert person.is_vaccinated
            assert person.infection is None
            did_survive += 1

        else:
            assert not person.is_alive
            assert not person.is_vaccinated
            assert person.infection is not None
            did_not_survive += 1

    print(f"Survived: {did_survive}")
    print(f"Did not survive: {did_not_survive}")

    # Stretch challenge! 
    # Check the infection rate of the virus by making a group of 
    # unifected people. Loop over all of your people. 
    # Generate a random number. If that number is less than the 
    # infection rate of the virus that person is now infected. 
    # Assign the virus to that person's infection attribute. 

    # Now count the infected and uninfect people from this group of people. 
    # The number of infectedf people should be roughly the same as the 
    # infection rate of the virus.