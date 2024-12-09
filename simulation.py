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

        # create a Logger object and bind it to self.logger
        self.logger = Logger('simulation_log.txt')

        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        # initializing other attributes needed
        self.population = self._create_population(initial_infected)
        self.newly_infected = []
    
    def _create_population(self, initial_infected):
        # initialize the population list
        population = []

        # the initial infected individuals
        for i in range(initial_infected):
            person = Person(i, False, self.virus)
            population.append(person)

        # the rest of the population
        for i in range(initial_infected, self.pop_size):
            is_vaccinated = (random.random() < self.vacc_percentage)
            person = Person(i, is_vaccinated)
            population.append(person)

        return population
        

    def _simulation_should_continue(self):
        
        for person in self.population:
            if person.is_alive and not person.is_vaccinated:
                return True
        return False

    def run(self):
        """
        Run the simulation. 
        The `virus` parameter is accepted for compatibility but not 
        used because the virus is already stored in the `Simulation` object.
        """

        time_step_counter = 0
        should_continue = True
        max_time_steps = 1000

        while should_continue and time_step_counter < max_time_steps:
            print(f'Starting time step {time_step_counter}')
            time_step_counter += 1
            self.time_step()
            should_continue = self._simulation_should_continue()
            self.logger.log_time_step(time_step_counter)
            self._infect_newly_infected()
        
        self.logger.write_metadata(self.pop_size, self.vacc_percentage, self.virus.name, self.virus.mortality_rate, self.virus.repro_rate)

        if time_step_counter >= max_time_steps:
            print("Reached maximum time steps, stop simulation.")
        else:
            print("Simulation finished.")

    def time_step(self):
        for person in self.population:
            if person.infection is not None and random.random() < self.virus.mortality_rate:
                person.is_alive = False

    def interaction(self, infected_person, random_person):
        if random_person.is_vaccinated:
            self.logger.log_interactions
        elif random_person.infection is not None:
            self.logger.log_interactions(infected_person._id, random_person._id, False, False, True)

        elif not random_person.is_vaccinated:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
                self.logger.log_interactions(infected_person._id, random_person._id, True, False, False)
                
            else:
                self.logger.log_interactions(infected_person._id, random_person._id, False, False, False)

    def _infect_newly_infected(self):
        for person in self.newly_infected:
            person.infection = self.virus

        self.newly_infected = []


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

    sim.run()
