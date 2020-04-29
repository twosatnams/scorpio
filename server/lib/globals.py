import os, sys, logging


logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger('logentries')
logger.setLevel(logging.DEBUG)

config = dict()
config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
config['OPERATION'] = os.environ.get('OPERATION')


class ApplicationException(Exception):
    pass
