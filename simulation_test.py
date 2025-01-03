from logger import Logger
from person import Person
from virus import Virus
from simulation import Simulation

def simulation_test():

    virus = Virus("HIV", 0.8, 0.3)

    sim = Simulation(virus, pop_size = 100, vacc_percentage=0.90, initial_infected=5)

    assert len(sim.population) == 100, f"Population size should be 100 but got {len(sim.population)}"

    initial_infected_count = sum(1 for person in sim.population if person.infection is not None)
    assert initial_infected_count == 5, f"Initial infected count should be 5 but got {initial_infected_count}"

    vaccinated_count = sum(1 for person in sim.population if person.is_vaccinated)
    expected_vaccinated = int(0.90 * (100 - 5))
    assert vaccinated_count == expected_vaccinated, f"Vaccinated count should be {expected_vaccinated} but got {vaccinated_count}"

    max_steps = 100
    for step in range(max_steps):
        print(f"Starting time step {step}")
        sim.time_step()
    
    print("All tests passed!")


# def simulation_test():

#     virus = Virus("Tuberculosis", 0.5, 0.6)

#     sim = Simulation(virus, pop_size = 100, vacc_percentage=0.90, initial_infected=5)

#     assert len(sim.population) == 100, f"Population size should be 100 but got {len(sim.population)}"

#     initial_infected_count = sum(1 for person in sim.population if person.infection is not None)
#     assert initial_infected_count == 5, f"Initial infected count should be 5 but got {initial_infected_count}"

#     vaccinated_count = sum(1 for person in sim.population if person.is_vaccinated)
#     expected_vaccinated = int(0.90 * (100 - 5))
#     assert vaccinated_count == expected_vaccinated, f"Vaccinated count should be {expected_vaccinated} but got {vaccinated_count}"

#     print("All tests passed!")

if __name__ == "__main__":
    simulation_test()