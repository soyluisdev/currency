import credentials
import requests
import pandas as pd

API_KEY = credentials.exchange_api_key

# Basic currency converter using API

url = 'https://v6.exchangerate-api.com/v6/{}/latest/USD'.format(API_KEY)

response = requests.get(url)
data = response.json()

currencies = pd.DataFrame.from_dict([data["conversion_rates"]])

print("\n")
print("Result: " + data['result'].title())
print("Documentation: " + data['documentation'].title())
print("Terms of Use: " + data['terms_of_use'].title())
print("Last Update UTC: " + data['time_last_update_utc'].title())
print("Next Update UTC: " + data['time_next_update_utc'].title())
print("\n")

nzd_mxn = (data['conversion_rates']['MXN'])/(data['conversion_rates']['NZD'])
usd_mxn = (data['conversion_rates']['MXN'])/(data['conversion_rates']['USD'])
values = (data['conversion_rates'])

# print("The value of NZD in mexican pesos is " + str(nzd_mxn))
# print("The value of USD in mexican pesos is " + str(usd_mxn))
print(currencies)
# convert_nzd = float(input("How many nzd you want to convert "))
# nzd_converted = convert_nzd * nzd_mxn
# print(str(convert_nzd) + " NZD" + " in mexican pesos is: " + str(nzd_converted))

