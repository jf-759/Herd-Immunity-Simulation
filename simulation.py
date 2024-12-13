import random, sys
# random.seed(42)
from person import Person
from logger import Logger
from virus import Virus


class Simulation(object):
    def __init__(self, virus, pop_size, vacc_percentage, initial_infected=1):

        self.virus = virus
        self.pop_size = pop_size
        self.vacc_percentage = vacc_percentage
        self.initial_infected = initial_infected

        self.total_interactions = 0
        self.total_infected = 0
        self.total_deaths = 0
        self.total_lives_saved_with_vaccine = 0


        # initializing other attributes needed
        self.population = self._create_population(initial_infected)
        self.newly_infected = []
    
    def _create_population(self, initial_infected):
        # initialize the population list
        population = []

        # the initial infected individuals
        for i in range(initial_infected):
            person = Person(i, is_vaccinated=False, infection=self.virus)
            population.append(person)

        num_vaccinated = int(self.vacc_percentage * (self.pop_size - initial_infected))

        # for those that are vaccinated
        for i in range(initial_infected, initial_infected + num_vaccinated):
            person = Person(i, is_vaccinated=True, infection=None)
            population.append(person)

        # for the rest of the population
        for i in range(initial_infected + num_vaccinated, self.pop_size):
            person = Person(i, is_vaccinated=False, infection=None)
            population.append(person)

        random.shuffle(population)
        return population

    def _simulation_should_continue(self):

        """ 
        Checks if the simulation should continue or not. 
        We check for any alive person (vaccinated or not).
        """
        
        for person in self.population:
            if person.is_alive:
                return True
        return False

    def run(self, time_steps):
        """
        Run the simulation. 
        The `virus` parameter is accepted for compatibility but not 
        used because the virus is already stored in the `Simulation` object.
        """

        time_step_counter = 0
        should_continue = True
    

        while should_continue and time_step_counter < time_steps:
            print(f'Starting time step {time_step_counter}')
            time_step_counter += 1

            self.time_step()

            should_continue = self._simulation_should_continue()

            self._infect_newly_infected()
        
        # Printing so I can see everything when running simulation.py
        infected_percentage = (self.total_infected / self.pop_size) * 100
        print(f"Percentage of the population that became infected: {infected_percentage}%")

        death_percentage = (self.total_deaths / self.pop_size) * 100
        print(f"Percentage of the population that died from the virus: {death_percentage}%")

        print(f"Total number of vaccinations that saved someone: {self.total_lives_saved_with_vaccine}")

        # Print output after simulation ends.
        print(f'{time_step_counter} {self.total_interactions} {self.total_infected} {self.total_deaths} {self.total_lives_saved_with_vaccine}')

        if time_step_counter >= time_steps:
            print(f"Simulation finished after {time_step_counter} time steps.")
        else:
            print("Simulation stopped early.")

    def time_step(self):
        
        # Simulate interactions between infected and healthy individuals
        for infected_person in [person for person in self.population if person.infection is not None and person.is_alive]:
            for random_person in [person for person in self.population if person.is_alive and person != infected_person]:
                self.interaction(infected_person, random_person)

            # Mortality rate
            if random.random() < self.virus.mortality_rate:
                infected_person.is_alive = False
                self.total_deaths += 1


    def interaction(self, infected_person, random_person):
        self.total_interactions += 1

        if random_person.is_vaccinated:
            self.total_lives_saved_with_vaccine += 1

        elif random_person.is_vaccinated == False and random_person.infection is None and random_person.is_alive:
            
            # if the person is unvaccinated and healthy, they may get infected
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.population.remove(random_person)
                self.total_infected += 1

    def _infect_newly_infected(self):
        """
        Infects everyone in the list then clears the list.
        """
        for person in self.newly_infected:
            person.infection = self.virus
            self.total_infected += 1
            self.population.append(person)

        self.newly_infected = []


# function to help with command-line arguements.
def load_config():
    # default values
    config = {
        'pop_size': 1000,
        'vacc_percentage': 0.1,
        'virus_name': 'Sniffles',
        'repro_rate': 0.5, 
        'mortality_rate': 0.12,
        'initial_infected': 10,
        'time_steps': 1000
    }

    if len(sys.argv) == 8:
        config['pop_size'] = int(sys.argv[1])
        config['vacc_percentage'] = float(sys.argv[2])
        config['virus_name'] = sys.argv[3]
        config['repro_rate'] = float(sys.argv[4])
        config['mortality_rate'] = float(sys.argv[5])
        config['initial_infected'] = int(sys.argv[6])
        config['time_steps'] = int(sys.argv[7])

    return config

if __name__ == "__main__":
    # Test your simulation here
    virus_name = "Sniffles"
    repro_num = 0.5
    mortality_rate = 0.12

    # Set some values used by the simulation
    pop_size = 1000
    vacc_percentage = 0.1
    initial_infected = 10


    # Make a new instance of the imulation
    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(virus, pop_size, vacc_percentage, initial_infected)
    config = load_config()

    sim.run(config['time_steps'])
