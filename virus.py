class Virus(object):
    # Properties and attributes of the virus used in Simulation.
    def __init__(self, name, repro_rate, mortality_rate):
        # Define the attributes of your your virus
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate



# Test this class
if __name__ == "__main__":
    # Test your virus class by making an instance and confirming 
    # it has the attributes you defined
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

    print(f'Virus name: {virus.name}\n Reproduction Rate: {virus.repro_rate * 100}% \n Mortality Rate: {virus.mortality_rate * 100}\n ')

    virus = Virus("Bird Flu", 0.4, 0.2)
    assert virus.name == "Bird Flu"
    assert virus.repro_rate == 0.4
    assert virus.mortality_rate == 0.2

    print(f'Virus name: {virus.name}\n Reproduction Rate: {virus.repro_rate * 100}% \n Mortality Rate: {virus.mortality_rate * 100}\n ')

    virus = Virus("COVID", 0.9, 0.4)
    assert virus.name == "COVID"
    assert virus.repro_rate == 0.9
    assert virus.mortality_rate == 0.4

    print(f'Virus name: {virus.name}\n Reproduction Rate: {virus.repro_rate * 100}% \n Mortality Rate: {virus.mortality_rate * 100}\n ')