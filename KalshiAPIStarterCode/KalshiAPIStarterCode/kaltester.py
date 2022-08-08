#kaltester

import KalshiClientsBase
import mysecrets

exch = KalshiClientsBase.ExchangeClient("https://trading-api.kalshi.com",mysecrets.locemail,mysecrets.locpass)

print("this is the kaltester speaking")

print(exch.get_balance())