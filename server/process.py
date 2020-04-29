from lib.globals import config
from lib.seed import seed_database

if config['OPERATION'] == 'SEED_DATA':
	seed_database()
else:
	print('WTF')