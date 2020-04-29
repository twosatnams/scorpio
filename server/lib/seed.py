from lib.models import Corporation, Stock, get_new_connection
from datetime import datetime
import random

corporations = [
	{'sym': 'MSFT', 'name': 'Microsoft Corporation', 'current_value': 169.81},
	{'sym': 'AAPL', 'name': 'Apple Inc.', 'current_value': 278.58},
	{'sym': 'AMZN', 'name': 'Amazon.com, Inc.', 'current_value': 2314.08},
	{'sym': 'GOOG', 'name': 'Alphabet Inc.', 'current_value': 1233.67},
	{'sym': 'FB', 'name': 'Facebook, Inc.', 'current_value': 182.91},
	{'sym': 'INTC', 'name': 'Intel Corporation', 'current_value': 58.75},
	{'sym': 'NVDA', 'name': 'NVIDIA Corporation', 'current_value': 291.36},
	{'sym': 'TSLA', 'name': 'Tesla, Inc.', 'current_value': 769.12},
	{'sym': 'CRM', 'name': 'Salesforce.com, inc.', 'current_value': 154.46},
	{'sym': 'PYPL', 'name': 'PayPal Holdings, Inc.', 'current_value': 116.14},
	{'sym': 'AMD', 'name': 'Advanced Micro Devices, Inc.', 'current_value': 55.51},
	{'sym': 'ATVI', 'name': 'Activision Blizzard, Inc.', 'current_value': 63.86},
	{'sym': 'EA', 'name': 'Electronic Arts Inc.', 'current_value': 111.35},
	{'sym': 'MTCH', 'name': 'Match Group, Inc.', 'current_value': 75.24}
]


def seed_database():
	db = get_new_connection()
	for corp in corporations:
		corporation = Corporation(name=corp['name'], symbol=corp['sym'])

		# Generate stock values between Jan 1, 2020 to Jan 31, 2020
		start_val = corp['current_value']
		for month_day in range(1, 32):
			stock = Stock(
				closing_value=round(start_val + random.uniform(-start_val/10, start_val/10), 2),
				highest_value=round(start_val + random.uniform(-start_val/10, start_val/10), 2),
				day_prediction_value=round(start_val + random.uniform(-start_val/10, start_val/10), 2),
				week_prediction_value=round(start_val + random.uniform(-start_val/10, start_val/10), 2),
				month_prediction_value=round(start_val + random.uniform(-start_val/10, start_val/10), 2),
				record_date=datetime(2020, 1, month_day)
			)
			corporation.stocks.append(stock)

		db.add(corporation)
		db.commit()
	db.close()





