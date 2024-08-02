import credentials
import requests

API_KEY = credentials.exchange_api_key

# Basic currency converter using API

url = 'https://v6.exchangerate-api.com/v6/{}/latest/USD'.format(API_KEY)

response = requests.get(url)
data = response.json()

nzd_mxn = (data['conversion_rates']['MXN'])/(data['conversion_rates']['NZD'])
usd_mxn = (data['conversion_rates']['MXN'])/(data['conversion_rates']['USD'])
values = (data['conversion_rates'])

print("The value of NZD in mexican pesos is " + str(nzd_mxn))
print("The value of NZD in mexican pesos is " + str(usd_mxn))

convert_nzd = float(input("How many nzd you want to convert "))
nzd_converted = convert_nzd * nzd_mxn
print(str(convert_nzd) + " NZD" + " in mexican pesos is: " + str(nzd_converted))

# for i, x in values.items():
#     print(i, x)