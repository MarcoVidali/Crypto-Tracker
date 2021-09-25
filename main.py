# Importings
import os
from rich import print
import cryptocompare



# Variables
cryptos_names = ["Bitcoin (BTC)", "Ethereum (ETH)", "Stellar (XLM)", "BinanceCoin (BNB)", "Cardano (ADA)", "Dogecoin (DOGE)", "XRP (XRP)", "Litecoin (LTC)", "BitcoinCash (BCH)", "Chainlink (LINK)"]



def main():   # Main function
    # Main loop
    while True:
        # Clearing console
        clearConsole()

        # Printing each crypto name and value
        for crypto_name in cryptos_names:   # Looping each crypto name
            crypto_acronymum = crypto_name.split(' ')[1].replace('(', '').replace(')', '')   # Getting crypto acronymum
            print(f"{blue(crypto_name)}{' ' * (30 - len(crypto_name))}{white(cryptocompare.get_price(crypto_acronymum)[crypto_acronymum]['EUR'])}")   # Printing crypto name and value

        # Waiting for user refresh
        input()

def clearConsole():
    command = 'clear'   # Creating command
    if os.name in ('nt', 'dos'):   # Checking if os is NT or DOS based
        command = 'cls'   # Changing command
    os.system(command)   # Executing command

def blue(string):   # Making blue string
    return f"[bold blue]{string}[/bold blue]"   # Returning blue string
    
def white(string):   # Making white string
    return f"[bold white]{string}[/bold white]"   # Returning white string



# Starting program
if __name__ == "__main__":
    main()