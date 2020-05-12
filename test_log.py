import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger('app')
logger.setLevel(logging.DEBUG)
handler = RotatingFileHandler('log/app.log', maxBytes=1024*1024, backupCount=2)
logger.addHandler(handler)

i=1
while i<10000:
    logger.info('test app')
    i += 1