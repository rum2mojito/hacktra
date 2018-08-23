import logging

logging.basicConfig(level=logging.DEBUG,
                        format='%(asctime)s %(filename)s %(lineno)s %(levelname)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers = [logging.FileHandler('log.txt', 'w', 'UTF-8'),])