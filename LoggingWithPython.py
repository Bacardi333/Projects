import logging

logging.basicConfig(level=logging.CRITICAL, format='{asctime} {levelname:<8} {message}', style='{', filename='%slog' % __file__[:-2], filemode='w')

username = 'Serg'

logging.debug('This is a debug msg')
logging.info('This is an info msg')
logging.warning('This is a warning msg')
logging.error('This is an error msg')
logging.critical('This is a critical msg')

a = 2
b = 0

try:
    mysum = a / b

except Exception as e:
    logging.critical('Exception occured:', exc_info=True)

logging.critical('There was an error with user: %s' % username)