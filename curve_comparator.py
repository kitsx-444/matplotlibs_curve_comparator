import matplotlib.pyplot as plt
from datetime import datetime

trades = {
	"EURUSD": [
		("2026-06-05", 45),
		("2026-06-01", -20),
		("2026-06-03", 60),
		("2026-06-02", 15),
		("2026-06-04", -10),
	],
	"GBPUSD": [
		("2026-06-03", -30),
		("2026-06-01", 25),
		("2026-06-05", 80),
		("2026-06-02", -15),
		("2026-06-04", 40),
	],
	"USDJPY": [
		("2026-06-01", 10),
		("2026-06-04", 10),
		("2026-06-02", 10),
		("2026-06-05", -50),
		("2026-06-03", 10),
	],
}

trade_date_format = '%Y-%m-%d'


# EURUSD Block
eu_starting_balance = 1000

eu_running_total = []
eu_real_dates = []
eurusd_sorted = sorted(trades['EURUSD'], key=lambda eu: eu[0])

for eu_date, eu_pips in eurusd_sorted:
	eu_starting_balance += eu_pips
	eu_running_total.append(eu_starting_balance)

	eu_real_date = datetime.strptime(eu_date, trade_date_format)
	eu_real_dates.append(eu_real_date)

# GBPUSD Block
gu_starting_balance = 1000

gu_running_total = []
gu_real_dates = []
gbpusd_sorted = sorted(trades['GBPUSD'], key=lambda gu: gu[0])

for gu_date, gu_pips in gbpusd_sorted:
	gu_starting_balance += gu_pips
	gu_running_total.append(gu_starting_balance)

	gu_real_date = datetime.strptime(gu_date, trade_date_format)
	gu_real_dates.append(gu_real_date)

# USDJPY Block
uj_starting_balance = 1000

uj_running_total = []
uj_real_dates = []
usdjpy_sorted = sorted(trades['USDJPY'], key=lambda uj: uj[0])

for uj_date, uj_pips in usdjpy_sorted:
	uj_starting_balance += uj_pips
	uj_running_total.append(uj_starting_balance)

	uj_real_date = datetime.strptime(uj_date, trade_date_format)
	uj_real_dates.append(uj_real_date)

plt.plot(eu_real_dates, eu_running_total, label='EURUSD')
plt.plot(gu_real_dates, gu_running_total, label='GBPUSD')
plt.plot(uj_real_dates, uj_running_total, label='USDJPY')
plt.legend()
plt.title('Multi-Pair Equity Curve Comparator')
plt.xlabel('Date')
plt.ylabel('Balance')
plt.show()
