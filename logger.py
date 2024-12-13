class Logger(object):
    def __init__(self, file_name):
        self.file_name = file_name

    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate, repro_rate):

        with open(self.file_name, 'w') as f:
            f.write(f'''
----------------------------------------------------------------------------------
|           Population Size: {pop_size}\n
|           Vaccination Percentage: {vacc_percentage}\n
|           Virus Name: {virus_name}\n
|           Mortality Rate: {mortality_rate}\n
|           Basic Reproduction Number: {repro_rate}\n
----------------------------------------------------------------------------------

                    
                    ''')

    def log_interactions(self, step_number, number_of_interactions, number_of_new_infections):
        '''
        Logs the details of interactions for a specific step.
        - step_number: The current step number in the simulation.
        - number_of_interactions: The total number of interactions during this step.
        - number_of_new_infections: The number of new infections that occurred this step.
        '''
        with open(self.file_name, 'a') as f:
            f.write (f'''
                
----------------------------------------------------------------------------------
|           Step Number: {step_number}\n
|           Number of Interactions: {number_of_interactions}\n
|           Number of New Infections : {number_of_new_infections}\n
----------------------------------------------------------------------------------

                ''')

    def log_infection_survival(self, step_number, population_count, number_of_new_fatalities):
        '''
        Logs the results of infection survival at each step.
        - step_number: The current step number in the simulation.
        - population_count: The total population count at this step.
        - number_of_new_fatalities: The number of new fatalities due to the infection.
        '''
        with open(self.file_name, 'a') as f:
            f.write(f'''

----------------------------------------------------------------------------------
|           Step Number: {step_number}\n
|           Total Population: {population_count}\n
|           Number of New Fatalities: {number_of_new_fatalities}\n
----------------------------------------------------------------------------------

                    ''')

    def log_time_step(self, time_step_number):
        '''
        Logs the completion of each time step.
        - time_step_number: The current time step number in the simulation.
        '''

        with open(self.file_name, 'a') as f:
            f.write(f'''
----------------------------------------------------------------------------------
|           Time Step Number: {time_step_number}\n
----------------------------------------------------------------------------------
                    ''')
            
    def log_interaction(self, infected_id, random_id, did_infect, is_vaccinated, was_alread_infected):
        with open(self.file_name, 'a') as f:
            f.write(f'''
----------------------------------------------------------------------------------
|           Infected Person {infected_id} interacts with Person {random_id}\n
|           Did infect: {did_infect}\n
|           Is vaccinated: {is_vaccinated}\n
|           Was already infected: {was_alread_infected}\n
----------------------------------------------------------------------------------
                    ''')