# Currency Converter

This project is a basic currency converter that uses the Exchange Rate API to convert New Zealand Dollars (NZD) and US Dollars (USD) to Mexican Pesos (MXN). It also includes a feature to convert a user-specified amount of NZD to MXN.

## Features

- **Real-Time Conversion Rates**: Uses the Exchange Rate API to fetch the latest currency conversion rates.
- **NZD and USD Conversion**: Calculates the value of 1 NZD and 1 USD in Mexican Pesos.
- **User-Specified Conversion**: Allows the user to enter an amount in NZD to see its value in MXN.

## Requirements

- **Python**: This project is written in Python and requires Python 3.x.
- **Requests Library**: Install via `pip install requests` to handle HTTP requests to the Exchange Rate API.
- **Exchange Rate API Key**: You will need an API key from [Exchange Rate API](https://www.exchangerate-api.com/).

## Setup

1. **Clone the repository** or download the code files.
2. **Create a `credentials.py` file** in the project directory with the following content:
    ```python
    exchange_api_key = 'YOUR_API_KEY'
    ```
    Replace `'YOUR_API_KEY'` with your actual API key.

3. **Run the script**:
    ```bash
    python currency_converter.py
    ```

## Usage

- **View Current Rates**: The script prints the latest conversion rates from USD and NZD to MXN.
- **Convert Amounts**: When prompted, enter an amount in NZD to convert it to MXN.

## Code Structure

- **`credentials.py`**: Stores the API key securely.
- **Main Script**: 
  - Fetches the latest exchange rates.
  - Calculates the exchange rate of NZD and USD to MXN.
  - Prompts the user to input an NZD amount for conversion.

## Sample Output

The value of NZD in Mexican Pesos is: 13.5 The value of USD in Mexican Pesos is: 18.3 How many NZD do you want to convert? 10 10 NZD in Mexican Pesos is: 135.0


## Future Improvements

- **Additional Currencies**: Allow the user to convert other currencies.
- **Error Handling**: Implement handling for API request failures or invalid user input.
- **Conversion History**: Log or display previous conversions.

## License

This project is open-source and can be modified or distributed.
