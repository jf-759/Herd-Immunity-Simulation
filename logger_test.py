# logger_test.py
from logger import Logger

def logger_test():
    logger = Logger('logger_test.txt')

    logger.write_metadata(100, 0.95, 'HIV', 0.3, 0.8)

    with open('logger_test.txt', 'r') as file:
        content = file.read()
        print(content)

if __name__ == "__main__":
    logger_test()