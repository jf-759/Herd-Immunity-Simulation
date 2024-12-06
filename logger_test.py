# logger_test.py
from logger import Logger

def logger_test():
    logger = Logger('logger_test.txt')
    logger.write_metadata(100, 0.95, 'HIV', 0.3, 0.8)

    # log interactions summary
    logger.log_interactions(1, 50, 10)

    # log infection survival
    logger.log_infection_survival(1, 90, 10)

    # Log time step
    logger.log_time_step(1)

    # verify the content
    with open('logger_test.txt', 'r') as file:
        content = file.read()
        print(content)
    

if __name__ == "__main__":
    logger_test()