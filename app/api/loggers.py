import logging


def create_logger():
    logger = logging.getLogger('basic')
    logger.setLevel('DEBUG')
    file_Handler = logging.FileHandler('app/api/logs/basic.txt')
    formatter_one = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
    file_Handler.setFormatter(formatter_one)
    logger.addHandler(file_Handler)
