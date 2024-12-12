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


# function to help with command-line arguements.
def load_config():
    # default values
    config = {
        'pop_size': 1000,
        'vacc_percentage': 0.1,
        'virus_name': 'Sniffles',
        'repro_rate': 0.5, 
        'mortality_rate': 0.12,
        'initial_infected': 10
    }

    if len(sys.argv) == 7:
        config['pop_size'] = int(sys.argv[1])
        config['vacc_percentage'] = float(sys.argv[2])
        config['virus_name'] = sys.argv[3]
        config['repro_rate'] = float(sys.argv[4])
        config['mortality_rate'] = float(sys.argv[5])
        config['initial_infected'] = int(sys.argv[6])

    return config

def run_simulation():
    config = load_config()
    virus = Virus(config['virus_name'], config['repro_rate'], config['mortality_rate'])
    sim = Simulation(config)
    sim.run()

def test_simulation():
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
